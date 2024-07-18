const express = require("express");
const fs = require("fs");
const childProcess = require("child_process");
const generator = require("project-name-generator");
const pokemon = require("pokemon");
const sqlite3 = require("sqlite3");
const cors = require("cors");
const formidable = require("formidable");

const db = new sqlite3.Database("./results.db");

const app = express();
const server = require("http").createServer(app);

app.use(cors());

// POST request to /api/assignments
app.post("/api/assignments", (req, res) => {
    const form = new formidable.IncomingForm();

    form.parse(req, (err, fields, files) => {
        if (err) {
            console.error("Error", err);
            throw err;
        }

        console.log("Fields", fields);

        let name = pokemon.random() + "-" + generator().dashed;

        const config = JSON.stringify({
            uid: name,
            test_cases: new Array(Number.parseInt(fields.testcases))
                .fill(undefined)
                .map((_, i) => ({
                    test_case: fields[`input${i + 1}`],
                    output: fields[`output${i + 1}`],
                    marks:
                        fields[`testWeight${i + 1}`] === "undefined"
                            ? 1
                            : Number.parseInt(fields[`testWeight${i + 1}`]),
                })),
        });
        fs.writeFileSync("/tmp/config.json", config);
        const zipFilePath = files.file.filepath;
        fs.renameSync(zipFilePath, zipFilePath + ".zip");

        console.log([
            "../friday/src/main.py",
            "-i",
            zipFilePath + ".zip",
            "-ti",
            "/tmp/config.json",
            "-lng",
            fields.language,
        ]);

        const proc = childProcess.spawn(
            "python3.10",
            [
                "../friday/src/main.py",
                "-i",
                zipFilePath + ".zip",
                "-ti",
                "/tmp/config.json",
                "-lng",
                fields.language,
            ],
            {
                stdio: "inherit",
            }
        );

        proc.on("exit", () => {
            const result = fs
                .readFileSync("../testResults.json")
                .toString("utf-8");
            
            db.run(
                "insert into results values (?,?)",
                [name, result],
                (err) => {
                    if (err) {
                        console.log(err);
                    }
                }
            );
            res.send(result);
        });
    });
});

app.post("/api/fetch_assignment", (req, res) => {
    const form = new formidable.IncomingForm();
    console.log("fetching");

    form.parse(req, (err, fields, files) => {
        if (err) {
            console.error("Error", err);
            throw err;
        }

        console.log("Fields", fields);

        db.get(
            "select * from results where uid = ?",
            [fields.assignmentName],
            (err, row) => {
                if (err) {
                    console.log(err);
                }
                res.send(row.result);
            }
        );
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));

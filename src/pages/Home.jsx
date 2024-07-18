import logo from "../assets/logo.png";
import "../App.css";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import { useState } from "react";
import Spinner from 'react-bootstrap/Spinner';
import io from "socket.io-client";
import { useNavigate } from "react-router-dom";
import testData from "../assets/testData.json";


const Home = () => {

    const supportedLanguages = ["C", "C++", "Java", "Python"];

    const [show, setShow] = useState(false);
    const [showResult, setShowResult] = useState(false);

    const [reqError, setReqError] = useState(false);

    const [testcase, setTestcase] = useState(1);

    //  useNavigate
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        file: null,
        testcases: 1,
        inputs: [],
        outputs: [],
        testWeights: [1],
        language: "C",
    });

    const [assName, setAssName] = useState({
        assignmentName: "",
    });

    const [loading, setLoading] = useState(false);

    function handleSubmit(e) {
        const data = new FormData();
        data.append("file", formData.file);
        data.append("testcases", formData.testcases);
        for (let i = 0; i < formData.testcases; i++) {
            data.append(`input${i + 1}`, formData.inputs[i]);
            data.append(`output${i + 1}`, formData.outputs[i]);
            data.append(`testWeight${i + 1}`, formData.testWeights[i]);
            data.append("language", formData.language);
        }
        setLoading(true);
        fetch("http://localhost:3000/api/assignments", {
            method: "POST",
            body: data,
        })
            .then((res) => res.json())
            .then((data) => {
                // handle data
                // setLoading(false);
                console.log(data);
                if(data.status == 400){
                    setReqError(true);
                    setLoading(false); 
                } else{
                    navigate('/dashboard', { state: { data: data } });
                }
            })
            .catch((err) => {
                // handle error
                // setLoading(false);
            });
    }

    function submitResult(e) {
        const data = new FormData();
        data.append("assignmentName", assName.assignmentName);
        setLoading(true);
        fetch("http://localhost:3000/api/fetch_assignment", {
            method: "POST",
            body: data,
        })
            .then((res) => res.json())
            .then((data) => {
                // handle data
                // setLoading(false);
                console.log(data);
                if(data.status == 400){
                    setReqError(true);
                    setLoading(false); 
                } else{
                    navigate('/dashboard', { state: { data: data } });
                }
            })
            .catch((err) => {
                // handle error
                // setLoading(false);
            });
    }

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const handleCloseResult = () => setShowResult(false);
    const handleShowResult = () => setShowResult(true);



    return (
        <div className="home-page">
            <div>
                <img src={logo} className="logo" alt="Friday logo" />
            </div>
            <h1>F.R.I.D.A.Y</h1>
            <div className="card-container">
                <p>Fast & Reliable Instructor's Digital Assessment System</p>
                <button className="small-rounded-btn" onClick={handleShow}>
                    Upload Assignment
                </button>

                <button className="small-rounded-btn" onClick={handleShowResult}>
                    Check Previous Assignment
                </button>

                <Modal show={showResult} onHide={handleCloseResult}>
                    <Modal.Header closeButton>
                        <Modal.Title>Retrieve Your Result</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <div className="form-group row">
                            <label htmlFor="assignment-name" className="col-3 col-form-label push-up">
                                Assignment Name
                            </label>
                            <div className="col-9">
                                <input

                                    className="form-control"
                                    id="assignment-name"
                                    name="assignment-name"
                                    placeholder="Assignment Name"
                                    type="text"
                                    required="required"
                                    onChange={(e) => {
                                        setAssName({
                                            assignmentName: e.target.value,
                                        });
                                    }}
                                />
                            </div>
                        </div>
                    </Modal.Body>

                    <Modal.Footer>
                        <Button
                            variant="secondary"
                            onClick={() => handleCloseResult()}
                        >
                            Close
                        </Button>
                        <Button
                            variant={loading ? "secondary" : "primary"}
                            onClick={() => {
                                submitResult();
                            }}
                            disabled={loading}

                        >
                            {loading ? (
                                <span>
                                    <Spinner animation="border" size="sm" variant="light" className="spinner" />
                                    Fetching Assignment
                                </span>
                            ) : (
                                "Fetch Assignment"
                            )}
                        </Button>
                    </Modal.Footer>
                </Modal>


                <Modal show={show} onHide={handleClose}>
                    <form onSubmit={handleSubmit}>
                        <Modal.Header closeButton>
                            <Modal.Title>New Assignment</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                            <div className="form-group row">
                                {/* Take a zip file as input */}
                                <label
                                    htmlFor="file"
                                    className="col-3 col-form-label push-up"
                                >
                                    Submission
                                </label>
                                <div className="col-9">
                                    <input
                                        className="form-control"
                                        id="file"
                                        name="file"
                                        placeholder="Zip File"
                                        accept=".zip"
                                        // Add a type of zip file only
                                        type="file"
                                        required="required"
                                        onChange={(e) => {
                                            setFormData({
                                                ...formData,
                                                file: e.target.files[0],
                                            });
                                        }}
                                    />
                                </div>
                                <div className="guidelines bottom-gap">
                                    Only Zip file containing code files with the
                                    submission guidelines are supported
                                </div>
                            </div>

                            {/* Take an input of number as dropdown upto max 10 number of test cases */}
                            <div className="form-group row">
                                <label
                                    htmlFor="testcases"
                                    className="col-3 col-form-label push-up"
                                >
                                    Number of Test Cases
                                </label>
                                <div className="col-9">
                                    <select
                                        className="form-control"
                                        id="testcases"
                                        name="testcases"
                                        onChange={(e) => {
                                            setTestcase(
                                                Number.parseInt(e.target.value)
                                            );
                                            setFormData({
                                                ...formData,
                                                testcases: Number.parseInt(
                                                    e.target.value
                                                ),
                                            });
                                        }}
                                    >
                                        {[...Array(10)].map((x, i) => (
                                            <option value={i + 1}>
                                                {i + 1}
                                            </option>
                                        ))}
                                    </select>
                                </div>
                            </div>

                            <div className="form-group row">
                                <label
                                    htmlFor="language"
                                    className="col-3 col-form-label push-up"
                                >
                                    Language
                                </label>
                                <div className="col-9 bottom-gap">
                                    <select
                                        className="form-control "
                                        id="language"
                                        name="language"
                                        onChange={(e) => {
                                            setFormData({
                                                ...formData,
                                                language:
                                                    e.target.value,
                                            });
                                        }}
                                    >
                                        {supportedLanguages.map((language) => (
                                            <option value={language}>
                                                {language}
                                            </option>
                                        ))}
                                    </select>
                                </div>
                            </div>

                            {/* Create a for loop for  inputs and outputs based on number of test cases */}
                            {[...Array(testcase)].map((x, i) => (
                                <div>
                                    <div className="form-group row">
                                        <label
                                            htmlFor={`input${i + 1}`}
                                            className="col-3 col-form-label push-up"
                                        >
                                            Input {i + 1}
                                        </label>
                                        <div className="col-9">
                                            <textarea
                                                className="form-control input-field"
                                                id={`input${i + 1}`}
                                                name={`input${i + 1}`}
                                                placeholder={`Enter Input ${i + 1
                                                    }`}
                                                required="required"
                                                onChange={(e) => {
                                                    let inputs =
                                                        formData.inputs;
                                                    inputs[i] = e.target.value;
                                                    setFormData({
                                                        ...formData,
                                                        inputs: inputs,
                                                    });
                                                }}
                                            />
                                        </div>
                                    </div>
                                    <div className="form-group row">
                                        <label
                                            htmlFor={`output${i + 1}`}
                                            className="col-3 col-form-label push-up"
                                        >
                                            Output {i + 1}
                                        </label>
                                        <div className="col-9">
                                            <textarea
                                                className="form-control output-field"
                                                id={`output${i + 1}`}
                                                name={`output${i + 1}`}
                                                placeholder={`Enter Output ${i + 1
                                                    }`}
                                                required="required"
                                                onChange={(e) => {
                                                    let outputs =
                                                        formData.outputs;
                                                    outputs[i] = e.target.value;
                                                    setFormData({
                                                        ...formData,
                                                        outputs: outputs,
                                                    });
                                                }}
                                            />
                                        </div>
                                    </div>
                                    <div className="form-group row bottom-gap">
                                        <label
                                            htmlFor={`testWeight${i + 1}`}
                                            className="col-3 col-form-label push-up"
                                        >
                                            Testcase Weightage
                                        </label>
                                        <div className="col-9">
                                            <select
                                                className="form-control test-weight"
                                                id={`testWeight${i + 1}`}
                                                name={`testWeight${i + 1}`}
                                                onChange={(e) => {
                                                    let testWeights =
                                                        formData.testWeights;
                                                    testWeights[i] = e.target.value;
                                                    setFormData({
                                                        ...formData,
                                                        testWeights: testWeights,
                                                    });
                                                }}
                                            >
                                                {[...Array(10)].map((x, i) => (
                                                    <option value={i + 1}>
                                                        {i + 1}
                                                    </option>
                                                ))}
                                            </select>
                                        </div>
                                    </div>

                                </div>
                            ))}
                        </Modal.Body>
                        <Modal.Footer>
                            <Button
                                variant="secondary"
                                onClick={() => handleClose()}
                            >
                                Close
                            </Button>
                            <Button
                                variant={loading ? "secondary" : "primary"}
                                onClick={() => {
                                    handleSubmit();
                                }}
                                disabled={loading}

                            >
                                {loading ? (
                                    <span>
                                        <Spinner animation="border" size="sm" variant="light" className="spinner" />
                                        Creating Assignment
                                    </span>
                                ) : (
                                    "Create Assignment"
                                )}
                            </Button>
                        </Modal.Footer>
                    </form>
                </Modal>
            </div>
        </div>
    );
};

export default Home;

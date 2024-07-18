import { Card } from "react-bootstrap"


const CardContainer = (props) => {

    const { students, totalMarks, totalTestCases } = props.data

    // students is an array of objects of the form for example:
    // {
    //     "roll": "123",
    //     "testcasesPassed": "2",
    //     "totalMarks": "5",
    // }

    const marksArray = students.map((student) => {
        return Number.parseInt(student.totalMarks)
    })

    const maxMarks = Math.max(...marksArray)
    const minMarks = Math.min(...marksArray)
    const avgMarks = marksArray.reduce(function (a, b) { return a + b; }, 0) / students.length

    const testCasesArray = students.map((student) => {
        return Number.parseInt(student.testcasesPassed)
    })

    const avgTestCases = testCasesArray.reduce(function (a, b) { return a + b; }, 0) / students.length

    const analysis = {
        "Maximum Marks": maxMarks,
        "Minimum Marks": minMarks,
        "Average Marks": avgMarks.toFixed(2),
        "Avg. No. of Testcase": avgTestCases.toFixed(2)
    }

    return (
        <div className="card-container2">
            {Object.entries(analysis).map((analysis) => {
                return (
                    <Card className="card-size">
                        <Card.Body>
                            <Card.Text className="card-text">{analysis[0]}</Card.Text>
                            <Card.Title className="card-title">
                                {analysis[1]}
                            </Card.Title>
                        </Card.Body>
                    </Card>
                )
            }
            )}
        </div>
    );
};

export default CardContainer;
import "../App.css";
import Navbar from "../components/Navbar";
import CardContainer from "../components/CardContainer";
// import line chart from frappe
import ReactFrappeChart from "react-frappe-charts";
import LineChart from "../components/LineChart";
import { ListGroup, Badge } from "react-bootstrap";
import { useLocation } from "react-router-dom";

const Dashboard = (props) => {

    const location = useLocation()

    console.log(location.state.data);

    const { uid, students, totalMarks, totalTestCases } = location.state.data;



    return (
        <div className="Dashboard">
            <Navbar />
            <div className="header-row">
                <h2>Statistics</h2>
                <h3>UID: 
                    <Badge
                    bg="warning"
                    pill
                    className="badge-container2"
                >
                    {uid}
                    </Badge>
                </h3>
            </div>


            <CardContainer data={location.state.data} />
            <h2>Charts</h2>
            <div className="chart-container">
                <LineChart
                    data={location.state.data}
                    title="Marks Distributiton"
                    which="marks"
                />
                <LineChart
                    data={location.state.data}
                    title="Testcases Passed"
                    which="testcase"
                />
            </div>
            
            <h2>Individual Performance</h2>

            <div className="list-container">
                <ListGroup as="ol" >
                    {students.map((student, index) => {
                        return (
                            <ListGroup.Item
                                as="li"
                                className="d-flex justify-content-between align-items-start"
                            >
                                <div className="ms-2 me-auto">
                                    <div className="fw-bold">
                                        Roll Number: {student.rollnumber}
                                    </div>
                                </div>
                                <Badge
                                    bg="primary"
                                    pill
                                    className="badge-container"
                                >
                                    {student.testcasesPassed} Test Cases
                                </Badge>
                                <Badge
                                    bg="success"
                                    pill
                                    className="badge-container"
                                >
                                    {student.totalMarks} Marks
                                </Badge>
                            </ListGroup.Item>
                        );
                    })}
                </ListGroup>
            </div>
        </div>
    );
};

export default Dashboard;

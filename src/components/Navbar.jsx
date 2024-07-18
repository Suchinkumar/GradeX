import '../App.css';
import { Container, Navbar } from "react-bootstrap"


const Nav = (props) => {
    return (
        <div className="Navbar">
            <Navbar>
                    <Navbar.Brand>Dashboard</Navbar.Brand>
                    <Navbar.Toggle />
                    <Navbar.Collapse className="justify-content-end">
                        <Navbar.Text>
                            Powered by <a href="/">F.R.I.D.A.Y</a>
                        </Navbar.Text>
                    </Navbar.Collapse>
            </Navbar>

        </div>
    )
}

export default Nav;
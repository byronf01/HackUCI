import "./login.css"

export default function Login() {
    return (
        <div className="login">
            <div className="loginWrapper">
                <div className="loginLeft">
                <h1 className="loginLogo">Deadly Hacks</h1>
                        <span className="loginDescription">
                            Join Deadly Hacks in connecting students and clubs around UCI.  
                        </span>
            </div>
                <div className="loginRight">
                    <div className="loginBox">
                            <input placeholder="Username" className="loginInput" />
                            <input placeholder="Password" className="loginInput" />
                            <button className="loginButton">Log In</button>
                            <span className="loginForgot" >Forgot Password?</span>
                            <button className="loginRegisterButton">Create New Account</button>
        </div>
        </div>
        </div>
        </div>
    )
}
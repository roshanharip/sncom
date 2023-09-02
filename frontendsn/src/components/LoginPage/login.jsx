
import { Fragment } from "react";
import Logo from '../../assets/logo.png';
import GoogleLogo from '../../assets/google.png';
import FacebookLogo from '../../assets/facebook.png';
import "./login.scss";
import {Form, FormGroup, Label, Input, Button} from 'reactstrap';
const Login = () => {

  return (
        <Fragment>
            <div className="Login">
                <nav className="LoginNav">
                    <div className="BgColor"></div>
                    <div className="LogoContainer">

                        <img src={Logo} alt="" className="LogoLogin"/>
                    </div>
                </nav>
                <main>
                    <div className="WelcomeTxt">
                        <h1>Welcome Back!</h1>
                        <h3>Log in to access your account</h3>
                    </div>
                    <div className="AuthContainer">
                        <div className="AuthWrapper">
                            <div className="SocialLogin">
                                <div className="LoginTxt">Login with</div>
                                <div className="LoginSocialLinks">
                                    <img src={GoogleLogo} alt="" />
                                    <img src={FacebookLogo} alt="" />
                                </div>
                            </div>
                            <div className="DivideLogin">
                                <div className="dimLine"></div>
                                <div>Or</div>
                                <div className="dimLine"></div>
                            </div>
                            <div className="AuthLogin">
                                <Form action="post">
                                    <FormGroup className="EmailGrp FrmGrp">
                                        <Label for="Email">
                                            Email
                                        </Label>
                                        <Input type="email" id="Email" />
                                    </FormGroup>
                                    <FormGroup className="FrmGrp PswdGrp">
                                        <Label for="CreatePass">
                                            Password
                                        </Label>
                                        <Input type="password" id="CreatePass" />
                                    </FormGroup>
                                    <Button>Login</Button>
                                </Form>
                            </div>
                            <div className="CreateAccount">Dont have an account? <span>SignUp</span></div>
                        </div>
                    </div>
                </main>
            </div>
        </Fragment>
    );
};

export default Login;

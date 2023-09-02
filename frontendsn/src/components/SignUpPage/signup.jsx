import { Fragment } from "react";
import Logo from '../../assets/logo.png';
import GoogleLogo from '../../assets/google.png';
import FacebookLogo from '../../assets/facebook.png';
import "./signup.scss";
import {Form, FormGroup, Label, Input, Button} from 'reactstrap';
const SignUp = () => {

  return (
        <Fragment>
            <div className="SignUp">
                <nav className="SignUpNav">
                    <div className="BgColor"></div>
                    <div className="LogoContainer">

                        <img src={Logo} alt="" className="LogoSignUp"/>
                    </div>
                </nav>
                <main>
                    <div className="WelcomeTxt">
                        <h1>Welcome!</h1>
                        <h3>SignUp to avail the services provided</h3>
                    </div>
                    <div className="AuthContainer">
                        <div className="AuthWrapper">
                            <div className="SocialSignUp">
                                <div className="signUpTxt">SignUp with</div>
                                <div className="signUpSocialLinks">
                                    <img src={GoogleLogo} alt="" />
                                    <img src={FacebookLogo} alt="" />
                                </div>
                            </div>
                            <div className="DivideSignUp">
                                <div className="dimLine"></div>
                                <div>Or</div>
                                <div className="dimLine"></div>
                            </div>
                            <div className="AuthSignUp">
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
                                    <FormGroup className="FrmGrp CPswdGrp">
                                        <Label for="ConfirmPass">
                                            Confirm Password
                                        </Label>
                                        <Input type="password" id="ConfirmPass" />
                                    </FormGroup>
                                    <Button>Sign Up</Button>
                                </Form>
                            </div>
                            <div className="AlreadyAccount">Have you account? <span>Login</span></div>
                        </div>
                    </div>
                </main>
            </div>
        </Fragment>
    );
};

export default SignUp;

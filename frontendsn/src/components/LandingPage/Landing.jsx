import { Fragment} from "react";
import "./Landing.scss";
import IntroImg from '../../assets/image1.png';
import Logo from '../../assets/logo.png';
import Illustration2 from '../../assets/image3.png';
import VideoIcon from '../../assets/services/video.svg';
import PharmacyIcon from '../../assets/services/pharmacy.svg';
import PathalogyIcon from '../../assets/services/pathalogy.svg';
import PhysiotherapyIcon from '../../assets/services/physiotherapy.png';
import AmbulanceIcon from '../../assets/services/ambulance.png';
import NursingBureauIcon from '../../assets/services/nursingbureau.png';
import ClinicIcon from '../../assets/services/clinic.png';
import HospitalIcon from '../../assets/services/hospital.png';
import ImagingCentresIcon from '../../assets/services/imagingcentres.png';
import QualitySrvIcon from '../../assets/whyus/qualityService.svg';
import AffordableIcon from '../../assets/whyus/Affordable.svg';
import MultipleOptIcon from '../../assets/whyus/multipleOpt.svg';
import FacebookIcon from '../../assets/social/facebook.svg';
import InstagramIcon from '../../assets/social/instagram.svg';
import EmailIcon from '../../assets/social/gmail.svg';
import TwitterIcon from '../../assets/social/twitter.svg';
import LocationMap from '../../assets/frame-30.png';
const Landing = () => {
    return (
        <Fragment>
            <div className="HomePage">
                <header className="HomeHeader">
                    <nav className="navLinks">
                        <img className="Logo" alt="" src={Logo} />
                        <div className="navBar">
                            <div className="aboutNavLink">About</div>
                            <div className="signupNavLink">Sign up</div>
                            <div className="loginNavLink">Login</div>
                        </div>
                    </nav>
                </header>
                <main className="Container">
                    <div className="Intro">
                        <div className="introChild IntroInfo">
                            <div className="WelcomeTxt">Welcome to</div>
                            <div className="CompanyName">SN COM PVT LTD</div>
                            <div className="IntroDes">Lorem ipsum dolor sit amet consectetur. Quam viverra nisl turpis commodo in placerat. Commodo massa pellentesque urna </div>
                        </div>
                        <div className="introChild IntroImgContainer">
                            <img className="IntroImg" alt="" src={IntroImg} />    
                        </div>
                    </div>
                    <div className="IllusSearchContainer">
                        <div className="IllustrationContainer">
                            <img className="IllustrationImg" alt="" src={Illustration2}/>
                        </div>
                        <div className="SearchBarContainer">
                            <div className="SearchBarWrapper">
                                <form action="post">
                                    <input type="search" name="search" id="searchServices" placeholder="Search for a service" />
                                    <button></button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div className="ServicesContainer">
                        <div className="ServicesTxt">Services Provided</div>
                        <div className="ServicesListContainer">
                            <div className="serviceChild VideoConsult" >
                                <img className="VideoConsultChild" alt="" src={VideoIcon} />
                                <div className="VideoConsultChildTxt">Online Video Consultation</div>
                            </div>
                            <div className="serviceChild Pharmacy">
                                <img className="PharmacyChild" alt="" src={PharmacyIcon} />
                                <div className="PharmacyChildTxt">Pharmacy</div>
                            </div>
                            <div className="serviceChild Pathalogy">
                                <img className="PathalogyChild" alt="" src={PathalogyIcon} />
                                <div className="PathalogyChildTxt">Pathology</div>
                            </div>
                            <div className="serviceChild Physiotherapy">
                                <img className="PhysiotherapyChild" alt="" src={PhysiotherapyIcon} />
                                <div className="PhysiotherapyChildTxt">Physiotherapy</div>
                            </div>
                            <div className="serviceChild NursingBureau">
                                <img className="NursingBureauChild" alt="" src={NursingBureauIcon} />
                                <div className="NursingBureauChildTxt">Nursing Bureau</div>
                            </div>
                            <div className="serviceChild Ambulance">
                                <img className="AmbulanceChild" alt="" src={AmbulanceIcon} />
                                <div className="AmbulanceChildTxt">Ambulance</div>
                            </div>
                            <div className="serviceChild Clinic">
                                <img className="ClinicChild" alt="" src={ClinicIcon} />
                                <div className="ClinicChildTxt">Clinic</div>
                            </div>
                            <div className="serviceChild Hospital">
                                <img className="HospitalChild" alt="" src={HospitalIcon} />
                                <div className="HospitalChildTxt">Hospital</div>
                            </div>
                            <div className="serviceChild ImagingCentres">
                                <img className="ImagingCentresChild" alt="" src={ImagingCentresIcon} />
                                <div className="ImagingCentresChildTxt">Imaging Centres</div>
                            </div>
                        </div>
                    </div>
                    <div className="WhyUsContainer">
                        <div className="WhyUsTxt">Why us ?</div>
                        <div className="WhyUsList">
                            <div className="whyUsChild QualityService">
                                <img className="QualityServiceChild" alt="" src={QualitySrvIcon} />
                                <div className="QualityServiceChildTxt">Quality Service</div>
                                <i className="QualityServiceChildDes">Borem ipsum dolor sit amet, consectetur adipiscing elit.</i>
                            </div>
                            <div className="whyUsChild MultipleOpt">
                                <img className="MultipleOptChild" alt="" src={MultipleOptIcon} />
                                <div className="MultipleOptChildTxt">Multiple options</div>
                                <i className="MultipleOptChildDes">Borem ipsum dolor sit amet, consectetur adipiscing elit. dolor sitamet</i>
                            </div>
                            <div className="whyUsChild Affordable">
                                <img className="AffordableChild" alt="" src={AffordableIcon} />
                                <div className="AffordableChildTxt">Affordable</div>
                                <i className="AffordableChildDes">Borem ipsum, consectetur adipiscing elit. dolor sit amet</i>
                            </div>
                        </div>
                    </div>
                </main>
                <footer className="Footer">
                    <div className="FootLinks">
                        <div className="ContactLinks">
                            <b className="b">+91 9999999999</b>
                            <b className="mail-us-at-container">
                                Mail us at<br/>
                                sncompvt@gmail.com
                            </b>
                        </div>
                        <div className="QuickLinks">
                            <div className="sign-up">Sign Up</div>
                            <div className="sign-up" >Log In</div>
                            <div className="gallery">Gallery</div>
                            <div className="gallery">FAQ</div>
                            <div className="gallery">Guides</div>
                            <div className="gallery">Blog</div>
                            <div className="gallery">Career</div>
                        </div>
                        <div className="LocationLinks">
                            <div className="locate-us">Locate us</div>
                            <img className="frame-item" alt="" src={LocationMap} />
                        </div>
                    </div>
                    <div className="SocialLinks">
                        <img className="FacebookIcon" alt="" src={FacebookIcon} />
                        <img className="TwitterIcon" alt="" src={TwitterIcon} />
                        <img className="InstagramIcon" alt="" src={InstagramIcon} />
                        <img className="EmailIcon" alt="" src={EmailIcon} />
                    </div>
                    <div className="Promote">@Designed by PrideTechGroup</div>
                </footer>
            </div>
        </Fragment>
    );
};

export default Landing;

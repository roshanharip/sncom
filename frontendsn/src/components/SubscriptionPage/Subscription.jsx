import { Fragment } from 'react';
import './Subscription.scss';
import Logo from '../../assets/logo.png';
import Cross from '../../assets/cross.svg';
import Tick from '../../assets/tick.svg';
const Subscription = () => {
    return(
        <Fragment>
            <div className="Subscription">
                <header className="SubHeader">
                    <nav className="navLinks">
                        <img className="Logo" alt="" src={Logo} />
                        <div className="navBar">
                            <div className="aboutNavLink">About</div>
                            <div className="faqNavLink">FAQs</div>
                        </div>
                    </nav>
                </header>
                <main className='SubMain'>
                    <div className='SubMainTxt'>
                        <div className='TitleTxt'>Choose the plan that works best for you</div>
                        <div className='CaptionTxt'>Select your plan and proceed to Pay</div>
                    </div>
                    <div className='SubPlanCards'>
                        <div className='GoldCard'>
                            <div className='GoldHead'>
                                <div className='GoldHeadChild'>
                                    <span>Gold</span>
                                    <span>Rs.1500</span>
                                </div>
                            </div>
                            <div className='GoldContent'>
                                <div className='GContentTxt'>Basic Features and services only</div>
                                <div className='GoldAccess'>
                                    <h4>Features</h4>
                                    <div className='FeaturesGold'>
                                        <div className='GoldItem'>
                                            <img src={Tick} alt="" />
                                            <div>limited Video Consultation</div>
                                        </div>
                                        <div className='GoldItem'>
                                            <img src={Tick} alt="" />
                                            <div>Home Devlivery</div>
                                        </div>
                                        <div className='GoldItem'>
                                            <img src={Tick} alt="" />
                                            <div>Pharmacy</div>
                                        </div>
                                        <div className='GoldItem'>
                                            <img src={Cross} alt="" />
                                            <div>Emergency Call</div>
                                        </div>
                                        <div className='GoldItem'>
                                            <img src={Cross} alt="" />
                                            <div>Pathalogy</div>
                                        </div>
                                        <div className='GoldItem'>
                                            <img src={Cross} alt="" />
                                            <div>24*7 Contact</div>
                                        </div>
                                    </div>
                                </div>
                                <div className='ButtonWrapper'>
                                    <button>
                                        Get Gold Plan
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div className='PreCard'>
                            <div className='PreRec'>Recommended</div>
                            <div className='PreHead'>
                                <div className='PreHeadChild'>
                                    <span>Premium</span>
                                    <span>Rs.2500</span>
                                </div>
                            </div>
                            <div className='PreContent'>
                                <div className='PContentTxt'>Premium Features and services only</div>
                                <div className='PreAccess'>
                                    <h4>Features</h4>
                                    <div className='FeaturesPre'>
                                        <div className='PreItem'>
                                            <img src={Tick} alt="" />
                                            <div>Unlimited Video Consultation</div>
                                        </div>
                                        <div className='PreItem'>
                                            <img src={Tick} alt="" />
                                            <div>Home Devlivery</div>
                                        </div>
                                        <div className='PreItem'>
                                            <img src={Tick} alt="" />
                                            <div>Pharmacy</div>
                                        </div>
                                        <div className='PreItem'>
                                            <img src={Tick} alt="" />
                                            <div>Emergency Call</div>
                                        </div>
                                        <div className='PreItem'>
                                            <img src={Tick} alt="" />
                                            <div>Pathalogy</div>
                                        </div>
                                        <div className='PreItem'>
                                            <img src={Tick} alt="" />
                                            <div>24*7 Contact</div>
                                        </div>
                                    </div>
                                </div>
                                <div className='ButtonWrapper'>
                                    <button>
                                        Get Premium Plan
                                    </button>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                    <div></div>
                </main>
            </div>
        </Fragment>
    );
}
export default Subscription;
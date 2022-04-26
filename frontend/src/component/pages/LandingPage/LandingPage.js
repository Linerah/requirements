import React, { Fragment } from "react";
import Footer from "../Footer/Footer";
import './LandingPage.css';

function LandingPage(){
    return(
        <div>
            <div className="background">
                <div className="center" >
                    <h1 className="landing-text" >Hello World!</h1>
                    <button className="landing-text" >Sign In</button>
                </div>
            </div>
        </div>
    );
}

export default LandingPage;
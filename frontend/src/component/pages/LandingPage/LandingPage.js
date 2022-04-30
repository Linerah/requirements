import React from "react";
import { Link } from "react-router-dom";
import './LandingPage.css';

function LandingPage(){
    return(
        <div>
            <div className="background">
                <div className="center" >
                    <h1 className="landing-text" >Welcome to the Condominium Gym Schedule Web App</h1>
                    <div className="inner" >
                        <div className="division" id="left" >
                            <Link to='/SignUp' className="button" >Sign Up</Link>
                        </div>
                        <div className="division" id="right" >
                            <Link to='/Login' className="button" >Login</Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default LandingPage;
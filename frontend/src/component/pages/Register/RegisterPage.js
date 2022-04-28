import React from 'react';
import './RegisterPage.css'
//import { Button } from "../../Button";

function Register() {
    return(
        <div classname='/Register'>
            <div classname='container-register'>
                <div>
                    <div>
                        <h1>Register Account</h1>
                        <div>
                            <input type='text' placeholder='Email' classname='credentials'/>
                        </div>
                        <div classname='confirm-email'>
                            <input type='text' placeholder='Confirm Email' classname='credentials'/>
                        </div>
                        <div classname='username-credentials'>
                            <input type='text' placeholder='Username' classname='credentials'/>
                        </div>                        
                        <div classname='password-credentials'>
                            <input type='password' placeholder='Password' classname='credentials'/>
                        </div>
                        <div classname='button-register'>
                            <button>Register</button>
                        </div>
                        <div classname='hyperlinks'>
                            Already have an account? <a href='#'>Login</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Register;
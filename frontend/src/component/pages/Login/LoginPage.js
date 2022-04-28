import React from 'react';
import './LoginPage.css'
//import { Button } from "../../Button";

function Login() {
    return(
        <div classname='/Login'>
            <div classname='container-login'>
                <div>
                    <div>
                        <h1>Login Page</h1>
                        <div>
                            <input type='text' placeholder='Username' classname='credentials'/>
                        </div>                        
                        <div classname='password-credentials'>
                            <input type='password' placeholder='Password' classname='credentials'/>
                        </div>
                        <div classname='button-login'>
                            <button>Login</button>
                        </div>
                        <div classname='hyperlinks'>
                            <a href='#'>Forgot Passwort?</a> or <a href='#'>Register</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Login;
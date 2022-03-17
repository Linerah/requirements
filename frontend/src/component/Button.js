import React from 'react';
import './Button.css';

const Styles = ['button--primary', 'button--outline']

const Sizes = ['button--medium', 'button--large', 'button--mobile', 'button--wide']

const Color = ['primary', 'blue', 'red', 'green']
//The Button is created, along with different parameters and behaviors that can be applied in any file; 
//colors are also included.
export const Button = ({
    children,
    type, 
    onClick, 
    buttonStyle, 
    buttonSize, 
    buttonColor}) => { 
        
    const checkButtonStyle = Styles.includes(buttonStyle) ? buttonStyle : Styles[0]

    const checkButtonSize = Styles.includes(buttonSize) ? buttonSize : Sizes[0]

    const checkButtonColor = Styles.includes(buttonColor) ? buttonColor : Color[1]

    return (
        <button className={`button ${checkButtonStyle} ${checkButtonSize} ${checkButtonColor}`} onClick={onClick} type={type}>
            {children}        
        </button>
    )
}
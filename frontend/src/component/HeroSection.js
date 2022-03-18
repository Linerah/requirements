import React from "react";
import { Button } from "./Button";
import { Link } from "react-router-dom";
import "./HeroSection.css";

import {useHistory}from 'react-router-dom';

function HeroSection({
  /* 
    Multiple parameters are listed here to highlight the contents and attributes of our sections.          
    This varies between the headlines, subtext, buttons and text and background color. Each one is seen in
    HeroSection.css in their tags which contain the finer details like letter size, font, alignment, etc. 
  */
  lightBg, 
  topLine,
  lightText,
  lightTextDesc,
  headline,
  description,
  buttonLabel,
  bool,
  img,
  alt,
  imgStart
}) {
  let history = useHistory();
  if(bool === false){
  return (   /* 
                This "Hero Section" is serving as a layout for when we want to build what each section will say
                or how it will look like. This will help making these sections easier, 
                the result of that is seen in the Data.js file. 
              */

                /*  
                  On top of that, what helps us make a light/dark background pattern, some conditionals are included to help with that.
                  For example, if we choose to add light text or a light background; or vice versa, then these changes will be seen. 
                  These colors can be seen in their respective tags in the .css file of this same name. 
                */
    <>
      <div
        className={lightBg ? "home__hero-section" : "home__hero-section darkBg"}
      >
        <div className="container">
          <div
            className="row home__hero-row"
            style={{
              display: "flex",
              flexDirection: imgStart === "start" ? "row-reverse" : "row"}}
          >
            <div className="col">
              <div className="home__hero-text-wrapper">
                <div className="top-line">{topLine}</div>
                <h1 className={lightText ? "heading" : "heading dark"}>    
                  {headline}
                </h1>
                <p
                  className={lightTextDesc ? "home__hero-subtitle" : "home__hero-subtitle dark"}>
                  {description}
                </p>
               
                  <Link to="/register">
                  <Button buttonSize="btn--wide" buttonColor="blue">
                    {buttonLabel}
                  </Button>
                </Link>
              </div>
            </div>

            <div className="col">
              <div className="home__hero-img-wrapper">
                <img src={img} alt={alt} className="home__hero-img" />
              </div>
            </div>
          </div>
        </div>
      </div>
    
    </>
  );
            }
            else{
              return (   /* 
                This "Hero Section" is serving as a layout for when we want to build what each section will say
                or how it will look like. This will help making these sections easier, 
                the result of that is seen in the Data.js file. 
              */

                /*  
                  On top of that, what helps us make a light/dark background pattern, some conditionals are included to help with that.
                  For example, if we choose to add light text or a light background; or vice versa, then these changes will be seen. 
                  These colors can be seen in their respective tags in the .css file of this same name. 
                */
    <>
      <div
        className={lightBg ? "home__hero-section" : "home__hero-section darkBg"}
      >
        <div className="container">
          <div
            className="row home__hero-row"
            style={{
              display: "flex",
              flexDirection: imgStart === "start" ? "row-reverse" : "row"}}
          >
            <div className="col">
              <div className="home__hero-text-wrapper">
                <div className="top-line">{topLine}</div>
                <h1 className={lightText ? "heading" : "heading dark"}>    
                  {headline}
                </h1>
                <p
                  className={lightTextDesc ? "home__hero-subtitle" : "home__hero-subtitle dark"}>
                  {description}
                </p>
               
                  <Link to="/register_doc">
                  <Button buttonSize="btn--wide" buttonColor="blue">
                    {buttonLabel}
                  </Button>
                </Link>
              </div>
            </div>

            <div className="col">
              <div className="home__hero-img-wrapper">
                <img src={img} alt={alt} className="home__hero-img" />
              </div>
            </div>
          </div>
        </div>
      </div>
    
    </>
  );
            }
  
}

export default HeroSection;

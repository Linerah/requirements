import React from "react";
import HeroSection from "../../HeroSection";
import { homeObjOne, homeObjThree } from "./Data";

function Home() {  //From the HeroSection files, the tags are included here so the text and different sections
                    //and the information we want to showcase will be seen on the HomePage.
  return (
    <div className = '/home'>
      {/* <HeroSection {...homeObjOne} />
      <HeroSection {...homeObjThree} /> */
      

      
      }
    </div>
  );
}

export default Home;
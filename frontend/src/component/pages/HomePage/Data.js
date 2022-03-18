/* Thanks to the HeroSection.js file, putting texts or images here is much simpler, */

/* These homeObjects will be included in Home.js which would be the Homepage of DOC */


export const homeObjOne = {
    lightBg: false,    // Declaring true or false in lightText, lightBg, or LightTextDesc, will result in this text being a dark 
    lightText: true,   // or light color. In HeroSection.js for example, if this lightText is delcared false, it will call on the .dark
    lightTextDesc: true, //version of this text, resulting in the dark color we choose it to be.   
    bool : false,
    topLine: 'Book anytime, anywhere',
    headline: "Doctor's Office Calendar",
    description: 'Get access to be able to book an appointment to an office and have it saved on your calendar.',
    buttonLabel: 'Get Started',
    buttonLabel1: null,
    imgStart: '',
}

export const homeObjThree = {
    lightBg: true,
    lightText: false,
    lightTextDesc: false,
    bool : true,
    topLine: 'Already a Doctor?',
    headline: "Get ahead by registering your office",
    description: 'By registering your office in the D.O.C database, your office will be viewed by users who are looking for appointments.',
    buttonLabel: 'Register Office',
    imgStart: ''

}
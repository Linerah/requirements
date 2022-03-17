import React, {useState, useEffect} from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Navbar from './component/Navbar';


function App() {
  
  const [data, setData] = useState([{}])

    useEffect(() => {
    fetch("/schedules").then( 
      res => res.json()
    ).then( 
        data => { 
            setData(data) 
            console.log(data) 
        }
      )
  }, [])

  return (
    <Router>
    <Navbar/>
    <Routes>
      {/* <Route exact path='/home' component={Home}/> */}
      {/* <Route exact path='/schedule' component={ScheduleSelector}/> */}
      {/* <Route exact path = '/login' component = {Login}/> */}
      {/* <Route exact path = '/register' component = {Register}/> */}
      {/* <Route exact path='/user_prof' component={ProfilePage}/> */}
    </Routes>
    {/* <Footer/> */}
  </Router>
  );
  

}

export default App
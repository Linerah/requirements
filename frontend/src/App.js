import Navbar from './component/Navbar';
import scheduleSelector from './component/pages/SchedulePage/SchedulePage';
import Home from './component/pages/HomePage/Home';
// import test from './component/pages/testPage/test';
import Footer from './component/pages/Footer/Footer';
import React, {useState, useEffect} from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"

function App() {
  
  const [data, setData] = useState([{}])
  const divStyle = {
    display: 'flex'
  }

    useEffect(() => {
    fetch("/schedules").then( 
      res => res.json()
    ).then( 
        data => { 
            setData(data) 
        }
      )
  }, [])

  // later is going to be used to remove time slot from the frontend
    const handleRemoveDay = (e) => {
    const name = e.target.getAttribute("name")
    let days = data.schedules
    let filter = []
    for(let day of days){
      if(day !== name){
        filter.push(day)
      }
    }  
    let newData = {'schedules': filter}
    setData(newData);
   };

  return (

    <Router>
    <Navbar/>
    <Switch>
      <Route exact path='/home' component={Home}/>
      <Route exact path='/schedule' component={scheduleSelector}/>
    </Switch>  
    <Footer/>
  </Router>
    

    
        //  {/* {(typeof data.schedules === 'undefined') 
        //   ? (<p>Loading...</p>)
        //   : 
        //   ( 
        //     data.schedules.map( (schedule, i) => (
        //       <div style={divStyle}> 
        //         <p key={i}>{schedule}</p>
        //         <button name={schedule} onClick={handleRemoveDay}>Schedule Day!</button>
        //       </div>
        //     ))

        //   )} */}

       
  )

 
}

export default App
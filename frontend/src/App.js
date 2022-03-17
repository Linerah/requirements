import React, {useState, useEffect} from 'react'

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
      <div>
        {(typeof data.schedules === 'undefined') 
          ? (<p>Loading...</p>)
          : 
          ( 
            data.schedules.map( (schedule, i) => (
              <div style={divStyle}> 
                <p key={i}>{schedule}</p>
                <button name={schedule} onClick={handleRemoveDay}>Schedule Day!</button>
              </div>
            ))

          )}

      </div>
  )

 
}

export default App
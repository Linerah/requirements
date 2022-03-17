import React, {useState, useEffect} from 'react'

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
      <div>
        {(typeof data.schedules === 'undefined') 
          ? (<p>Loading...</p>)
          : ( 
            data.schedules.map( (schedule, i) => (
              <p key={i}>{schedule}</p>
            ))

          )}

      </div>
  )
}

export default App
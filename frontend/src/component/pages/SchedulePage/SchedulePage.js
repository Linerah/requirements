import ScheduleSelector from 'react-schedule-selector';
import { Link } from "react-router-dom";
import React, {Component} from 'react'
import Paper from '@material-ui/core/Paper';
 
class scheduleSelector extends Component {
  state = { schedule : [] }
 
  handleChange = newSchedule => {
    this.setState({ schedule: newSchedule })
  }
  // renderCustomDateCell = (time, selected, innerRef) => (
  //   <div style={{ textAlign: 'center' }} ref={innerRef}>
  //     {selected ? '❌' : '✅'}
  //   </div>
  // )
  render() {
    return (
      <div style={{ margin: "0 auto", width: "100%" }}>
      <ScheduleSelector
        selection={this.state.schedule}
        numDays={7}
        minTime={5}
        maxTime={22}
        hourlyChunks={1}
        // renderDateCell={this.renderCustomDateCell}
        onChange={this.handleChange}
      />
      </div>
    );
  }
}
export default scheduleSelector
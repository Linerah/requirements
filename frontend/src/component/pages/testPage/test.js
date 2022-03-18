import React from 'react'

import Paper from '@material-ui/core/Paper';
import { ViewState } from '@devexpress/dx-react-scheduler';
import {
  Scheduler,
  DayView,
  WeekView,
  MonthView,
  Appointments,
} from '@devexpress/dx-react-scheduler-material-ui';

export function getCurrentDate(separator=''){

  let newDate = new Date()
  let date = newDate.getDate();
  let month = newDate.getMonth() + 1;
  let year = newDate.getFullYear();
  
  return `${year}${separator}${month<10?`0${month}`:`${month}`}${separator}${date}`
  }

const currentDate = getCurrentDate();
const schedulerData = [
  { startDate: '2021-11-27T09:45', endDate: '2021-11-27T11:00', title: 'Meeting' },
  { startDate: '2021-11-27T12:00', endDate: '2021-11-27T13:30', title: 'Go to a gym' },
];

export default () => (
  <Paper>
    <Scheduler
      data={schedulerData}
    >
      <ViewState
        currentDate={currentDate}
      />
      <WeekView
        startDayHour={9}
        endDayHour={19}
      />
      <Appointments />
    </Scheduler>
  </Paper>
);
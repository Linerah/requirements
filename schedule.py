from timeslot import TimeSlot


class Schedule:
    def __init__(self, starting_day, ending_day, starting_hour, ending_hour):
        self.days = self.generate_days(starting_day, ending_day, starting_hour, ending_hour)
        self.starting_day = starting_day
        self.ending_day = ending_day
        self.starting_hour = starting_hour
        self.ending_hour = ending_hour


    # this methods generates the list of days expecified with its timeslots,
    # return dict_days(start_day to end_day)
    def generate_days(self, starting_day, ending_day, starting_hour, ending_hour):
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        days = {}
        starting = False
        for day in week:
            if(starting_day == day):
                starting = True
            if(starting):  
                days[day] = self.generate_timeslots(day, starting_hour, ending_hour)
            if(ending_day == day):
                break
        return days

    # Generates the timeSlots of each day, returns a list of TimeSlots
    def generate_timeslots(self, day, starting_hour, ending_hour):
        time_slots = []
        for hour in range(starting_hour, ending_hour + 1):
            time_slots.append(TimeSlot(hour, day))   
        return time_slots

    def generate_json_format(self):
        json = {}
        for day in self.days:
            json[day] = []
            for timeslot in self.days[day]:
                json[day].append(timeslot.convert_dict()) 
        return json

    def get_timeslot(self, day, hour) -> TimeSlot:
        for timeslot in self.days[day]:
            if timeslot.hour == hour:
                return timeslot
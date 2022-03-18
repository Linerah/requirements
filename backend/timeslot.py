from unittest import result


class TimeSlot:
    def __init__(self, hour, day):
        self.users_interested = []
        self.hour = hour
        self.day = day
        self.user = None

    def add_user(self, new_user):
        self.user = new_user

    def add_user_interested(self, new_user):
        self.users_interested.append(new_user)
    
    def __str__(self):
        result = []
        result.append(f'Timeslot(day: {self.day}, hour: {self.hour}, user: {self.hour}, users interested: ')
        for user in self.users_interested:
            result.append(user)
            result.append(', ')
        del result[-1]
        result.append(')')
        return ''.join(result)

    def convert_dict(self):
        return {'time': self.hour, 'day': self.day, 'user': self.user, 'users_interested': self.users_interested}

    def is_full(self):
        return self.user != None
        

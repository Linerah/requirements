from unittest import result

from flask import jsonify


class TimeSlot:
    def __init__(self, time, day):
        self.users_interested = []
        self.time = time
        self.day = day
        self.username = None
    
    @staticmethod
    def create_timeslot(time, day, database):
        timeslot = TimeSlot(time, day)
        timeslot_document = timeslot.convert_json()
        collection = database.db.timeslots
        print(timeslot_document)
        collection.insert_one(timeslot_document)
        return timeslot
    
    @staticmethod
    def get_timeslots(database):
        collection = database.db.timeslots
        timeslots = str(list(collection.find()))
        return timeslots

    @staticmethod
    def get_user_timeslots(database, username):
        collection = database.db.timeslots
        timeslots = collection.find({'username': username})
        return timeslots

    @staticmethod
    def set_reservation(database, username, day, time):
        collection = database.db.timeslots
        if collection.find_one({'day':day, 'time':time})['username'] == None:
            collection.update_one({'day':day, 'time':time},{'username': username})
            return jsonify({'day':day, 'time':time, 'username': username})
        else:
            return jsonify({'error':'Time is already taken'})

    def add_user(self, new_user):
        self.username = new_user.username

    def add_user_interested(self, new_user):
        self.users_interested.append(new_user)
    
    def __str__(self):
        result = []
        result.append(f'Timeslot(day: {self.day}, time: {self.time}, username: {self.username}, users interested: ')
        for user in self.users_interested:
            result.append(user)
            result.append(', ')
        del result[-1]
        result.append(')')
        return ''.join(result)

    def convert_json(self):
        return {'time': self.time, 'day': self.day, 'username': self.username, 'users_interested': self.users_interested}

    def is_full(self):
        return self.username != None
        
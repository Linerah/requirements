from crypt import methods
import os
from flask import Flask, jsonify, render_template, url_for, request
from flask_pymongo import PyMongo
from datetime import datetime
from timeslot import TimeSlot
from user import User
from schedule import Schedule
import certifi
import secrets


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'scheduler_db'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin2:" + os.environ.get("MONGO_PW") + "@cluster0.vq3ym.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app, tlsCAFile=certifi.where())

# run this the first time, to create the collection
# mongo.db.create_collection('timeslots')

# -- Session data --
app.secret_key = secrets.token_urlsafe(16)


# Fake users - DB
kevin = User("kevlin","kevlin@whereever.com", "a12341231")
fernando = User("fernan1", "fernan@whereever.com", "b5678567857")
sebastian = User("sebastian12", "sebas@whereever.com", "c0000000000")
all_users= {"kevlin": kevin, "fernan1": fernando, "sebastian12": sebastian}

# Days of the week
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

@app.route("/get_timeslots")
def get_timeslots():    
    return TimeSlot.get_timeslots(mongo)

@app.route("/get_user_timeslots/<username>")
def get_user_timeslots(username): 
    return jsonify(TimeSlot.get_user_timeslots(mongo, username))

@app.route("/set_reservation/<username>")
def set_reservation(username): 
    info = request.get_json(force=True)
    day = info['day']
    time = info['time']  
    return TimeSlot.set_reservation(mongo, username, day, time)
   
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.get_json(force=True)
        print(user)
        username = user['username']
        email = user['email']
        password = user['password']
        # If Username is not in database
        user = User.get_user(mongo, username)
        if not user:
            user = User.create_user(mongo, username, email, password)
            return jsonify(user)
        return jsonify({'error': 'Username already exists'}) 
    return jsonify({'error': "GET is not a valid request"}) 

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_json = request.get_json(force=True)
        password = user_json['password']
        username = user_json['username']
        user = User.get_user(mongo, username)
        #If user is in the database 
        if user:
            if user['password'] == password:
                print(user)
                return user
            else:
                return 'Username or password are incorrect' 
        return 'User does not exist' 
    return "GET is not a valid request"
      
@app.route("/get_users")
def get_users():    
    return jsonify(User.get_users(mongo))

if __name__ == "__main__":
    app.run(debug=True)
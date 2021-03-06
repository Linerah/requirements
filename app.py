#from crypt import methods
import os
import sched
from flask import Flask, jsonify, redirect, render_template, url_for, request, session
from flask_pymongo import PyMongo
from datetime import datetime
from timeslot import TimeSlot
from user import User
from schedule import Schedule
import certifi
import secrets
from collections import defaultdict

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'scheduler_db'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin2:" + os.environ.get("MONGO_PW") + "@cluster0.vq3ym.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app, tlsCAFile=certifi.where())
# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

# department set:
departments = {"Women", "Men"}

# Fake users - DB
kevin = User("kevlin","kevlin@whereever.com", "a12341231")
fernando = User("fernan1", "fernan@whereever.com", "b5678567857")
sebastian = User("sebastian12", "sebas@whereever.com", "c0000000000")
all_users= {"kevlin": kevin, "fernan1": fernando, "sebastian12": sebastian}

# Days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
timeslots = ["5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM","12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM",  "4:00 PM",  "5:00 PM"]

# -- Routes section --
# LOGIN Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        user = User.get_user(mongo, username)
        if not user:
            return render_template("login.html", message="User not found")
        else:
            password = request.form["password"]
            password_correct = user.compare_password(password)
            if password_correct:
                session["username"] = request.form["username"]
                return redirect("/schedule")
            else:
                return render_template("login.html", message="Incorrect password")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        user = User.get_user(mongo, username)
        if not user:
            try:
                user = User.create_user(mongo,username, email, password)
                session["username"] = request.form["username"]
                return redirect("/schedule")
            except:
                return render_template(
                    "login.html", message="Invalid email, username or password"
                )
        elif user["email"] == email:
            return render_template("login.html", message="Email already exists")
        else:
            return render_template("login.html", message="Username already exists")


# LOGOUT Route
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# LANDING Route
@app.route("/")
@app.route("/landing")
def landing():
    return render_template("landing.html")

@app.route("/seed_items")
def seed_items():
  pass

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

# SCHEDULE Route
@app.route("/schedule")
def schedule():
    reserved = defaultdict(set)
    
    for timeslot in TimeSlot.get_reserved_timeslots(mongo):
        reserved[timeslot['day']].add(timeslot['time'])
    print(reserved)
    if session:
        return render_template("schedule.html", days=days, timeslots=timeslots, reserved=reserved)
    return "Error authentication failed."

@app.route("/schedule_confirm/<schedule>", methods = ["GET", "POST"])
def schedule_confirm(schedule):
    day_time = schedule.split(" ")
    day = day_time[0]
    time =  day_time[1] + " " + day_time[2]
    if session:
        if request.method == "GET":
            return render_template("scheduleConfirm.html", day=day, time=time, schedule=schedule)
        if request.method == "POST":
            time = request.form['time']
            day = request.form['day']
            TimeSlot.set_reservation(mongo, session['username'], day, time)
            return redirect("/profile")
    return "Error authentication failed."        


# ADMIN-Manage Schedule page Route
@app.route("/admin_manage")
def admin_manage():
    timeslots = TimeSlot.get_reserved_timeslots(mongo)
    for timeslot in timeslots:
        print(timeslot)
    return render_template("indexSchedule.html", timeslots=timeslots)

# ADMIN- Users page Route
@app.route("/admin_users")
def admin_users():
    users = User.get_users(mongo)
    return render_template("indexUsers.html", users=users)



# ADMIN-CreateSchedule page Route
@app.route("/admin_schedule")
def admin_schedule():

    return render_template("createSchedule.html")

@app.route("/admin_users_edit/<id>", methods=['POST'])
def admin_users_edit(id):
    user = User.get_user_by_id(mongo, id)
    new_username = request.form['username']
    new_email = request.form['email']
    new_rank = request.form['rank']
    print(new_username)
    print(new_email)
    print(new_rank)
    #Must be done this way since HTML returns as a string!
    if new_rank == 'True':
        user.update_user(mongo, id, new_username, new_email, True)
    else:
        user.update_user(mongo, id, new_username, new_email, False)
    return redirect(url_for('admin_users'))

@app.route("/admin_users_del/<id>", methods=['POST'])
def admin_users_del(id):
    User.delete_user(mongo, id)
    return redirect(url_for('admin_users'))
    
@app.route("/profile")
def user_prof():
    if session:
        user = User.get_user(mongo, session["username"]) 
        reservations = TimeSlot.get_user_timeslots(mongo, session["username"])

        return render_template("user_profile.html", reservations=reservations, user=user)
    else:
        return "Error authentication failed."


@app.route("/seed")
def seed():
    TimeSlot.create_timeslot("7:00 AM", "Friday", mongo)
    TimeSlot.create_timeslot("9:00 AM", "Friday", mongo)
    TimeSlot.create_timeslot("5:00 PM", "Monday", mongo)
    return "Successful"
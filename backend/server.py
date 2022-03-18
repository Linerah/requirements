from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from schedule import Schedule


app = Flask(__name__)
  

schedule = Schedule('Monday', 'Friday', 6, 18) # M-F 6am-6pm


# Schedule API Route
@app.route('/schedule')
def generate():
    # JSON array / dictionary 
    # return {"schedules": ["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday"]}
    return schedule.generate_json_format()



@app.route('/selectedtime', methods = ['POST'])
def member_selected_time(): 
    user = request.form['user']
    day = request.form['day']
    hour = request.form['hour']
    # user -> null vacion
    # user != null lleno
    timeslot = schedule.get_timeslot(day, hour)
    if (timeslot.is_full()):
        return "Timeslot is already full" #Placeholder
    timeslot.add_user(user)



if __name__ == "__main__":
    app.run(debug=True)
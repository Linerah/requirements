import email
from enum import unique
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_scheduled = db.Column(db.String(200), nullable=False)
    time_scheduled = db.Column(db.String(200), nullable=False)
    user = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<Schedule {self.id}, booked at {self.date_created}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.id}')"

class SlotTime(db.Model): # The slot time can have the start and end time, how many spaces available in the specific time slot
    start_time = db.Column(db.Integer, nullable=False) #Maybe have the time in military format (####;0800=8:00) and then convert to actual time?
    end_time = db.Column(db.Integer, nullable=False)
    isAvailable = db.Column(db.Boolean, default=True, nullable=False) #Check if this works
    
    def __repr__(self):
        return f"Slot Time from {self.start_time} to {self.end_time}, Available: {self.isAvailable}"


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
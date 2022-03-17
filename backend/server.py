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

# Schedule API Route
@app.route('/schedules')
def schedules():
    # JSON array / dictionary 
    return {"schedules": ["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday"]}

if __name__ == "__main__":
    app.run(debug=True)
import datetime

from sqlalchemy import String, Integer, DateTime

from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), unique=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, task_name):
        self.task_name = task_name

    def __repr__(self):
        return f'<Task {self.task_name}>'

    def to_json(self):
        return {
            'id': self.id,
            'task_name': self.task_name,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }

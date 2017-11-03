from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI, status, exceptions

from app.errors import InvalidParameter


app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models import Task

@app.route('/tasks', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        tasks = Task.query.all()
        results = []
        for task in tasks:
            res = {
                'id': task.id,
                'task_name': task.task_name,
                'date_created': task.date_created,
                'date_modified': task.date_modified
            }
            results.append(res)
        return results, status.HTTP_201_CREATED
    elif request.method == 'POST':
        if 'task_name' in request.data:
            task_name = request.data['task_name']
            if task_name:
                new_task = Task(task_name=task_name)
                db.session.add(new_task)
                db.session.commit()
                response = {
                    'id': new_task.id,
                    'task_name': new_task.task_name,
                    'date_created': new_task.date_created,
                    'date_modified': new_task.date_modified
                }
                return response, status.HTTP_201_CREATED
        raise InvalidParameter


@app.route('/tasks/<int:id>', methods=['GET', 'DELETE'])
def manage_tasks(id):
    task = Task.query.filter_by(id=id).first()
    if not task:
        raise exceptions.NotFound()
    if request.method == 'GET':
        response = {
            'id': task.id,
            'name': task.task_name,
            'date_created': task.date_created,
            'date_modified': task.date_modified
        }
        return response
    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return {
            'message': f'task {task.id} deleted'
        }

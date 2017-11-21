from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI, status
from sqlalchemy.exc import IntegrityError

from app.errors import InvalidParameter, TaskNotFound


app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models import Task


@app.route('/tasks', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        tasks = Task.query.all()
        results = [t.to_json() for t in tasks]
        return results, status.HTTP_201_CREATED
    elif request.method == 'POST':
        if 'task_name' in request.data:
            task_name = request.data['task_name']
            try:
                if task_name:
                    new_task = Task(task_name=task_name)
                    db.session.add(new_task)
                    db.session.commit()
                    response = new_task.to_json()
                    return response, status.HTTP_201_CREATED
            except IntegrityError:
                return {'error': 'This task already exists'}
        raise InvalidParameter


@app.route('/tasks/<int:id>', methods=['GET', 'DELETE'])
def manage_tasks(id):
    task = Task.query.filter_by(id=id).first()
    if not task:
        raise TaskNotFound
    if request.method == 'GET':
        response = task.to_json()
        return response
    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return {
            'message': f'task {task.id} deleted'
        }


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

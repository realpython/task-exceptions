from flask import jsonify, request
from flask_api import status, exceptions

from app import app, db
from app.models import Task


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

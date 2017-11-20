from flask_api.exceptions import APIException


class InvalidParameter(APIException):
    status_code = 404
    detail = 'Invalid parameters'


class TaskNotFound(APIException):
    status_code = 404
    detail = 'This task does not exist'

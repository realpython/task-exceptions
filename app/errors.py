from flask_api.exceptions import APIException


class InvalidParameter(APIException):
    status_code = 404
    detail = 'Invalid parameters'

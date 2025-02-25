from flask import jsonify


class HttpError(Exception):
    def __init__(self, status_code: int, message: str | list| dict):
        self.status_code = status_code
        self.message = message


def error_handler(error: HttpError):
    response = jsonify({'status': 'error', 'message': error.message})
    response.status_code = error.status_code

    return response

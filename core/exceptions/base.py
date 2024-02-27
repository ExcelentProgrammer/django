from rest_framework.exceptions import APIException


class InvalidConfirmationCodeException(Exception):
    def __init__(self, message):
        self.message = message


class IsBlockException(Exception):

    def __init__(self, message, expired):
        self.message = message
        self.expired = expired


class SmsNotFoundException(Exception):
    def __init__(self, message):
        self.message = message


class IsExpiredException(Exception):
    def __init__(self, message):
        self.message = message


class BreakException(Exception):

    def __init__(self, *args, message: str = None, data=None):
        if data is None:
            data = []
        self.args = args
        self.message = message
        self.data = data


class MyApiException(APIException):
    status_code = 400

    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

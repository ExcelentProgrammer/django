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

    def __init__(self, *args, message: str = None, data: dict | list = []):
        self.args = list(args)
        self.message = message
        self.data = data

from rest_framework import status
from rest_framework.exceptions import APIException


class ResponseException:

    def __init__(self, message="", data=None, error_code=0, status_code=status.HTTP_400_BAD_REQUEST):
        if data is None:
            data = []
        response = {
            "success": False,
            "message": message,
            "data": data,
            "error_code": error_code
        }
        raise APIException(response, status_code)

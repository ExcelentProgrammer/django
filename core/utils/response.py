from rest_framework import status
from rest_framework.response import Response


class ApiResponse:
    @staticmethod
    def success(message="", data=None, status_code=status.HTTP_200_OK, **meta):
        if data is None:
            data = []
        response = {
            "success": True,
            "message": message,
            "data": data,
            **meta
        }
        return Response(data=response, status=status_code)

    @staticmethod
    def error(message="", data=None, error_code=0,
              status_code=status.HTTP_400_BAD_REQUEST):
        if data is None:
            data = []
        response = {
            "success": False,
            "message": message,
            "data": data,
            "error_code": error_code
        }
        return Response(response, status_code)
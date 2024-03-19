from rest_framework import status
from rest_framework.response import Response

from core.exceptions import (
    BreakException, MyApiException
)


class ApiResponse:
    @staticmethod
    def success(
            message="", data=None,
            status_code=status.HTTP_200_OK, **meta
    ):
        if data is None:
            data = []
        response = {
            "success": True, "message": message,
            "data": data, **meta
        }
        return Response(data=response, status=status_code)

    @staticmethod
    def error(
            message="", data=None,
            error_code=0, status_code=status.HTTP_400_BAD_REQUEST,
            exception=None, **kwargs
    ):

        #####################
        # Ignore BreakException
        #####################
        if isinstance(exception, BreakException):
            raise exception

        if data is None:
            data = []
        response = {
            "success": False, "message": message,
            "data": data, "error_code": error_code,
            **kwargs
        }
        raise MyApiException(response, status_code)

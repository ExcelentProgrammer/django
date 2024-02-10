from rest_framework import status
from rest_framework.response import Response


class BaseService:
    """ Test Service Base """

    @staticmethod
    def success(data, status=status.HTTP_200_OK):
        response = {
            "success": True,
            "data": data
        }
        return Response(data=response, status=status)

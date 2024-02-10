import logging

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from core.http.serializers import AuthSerializer
from core.http.tasks import my_task
from core.services.BaseService import BaseService


class Auth(APIView, BaseService):
    serializer_class = AuthSerializer

    def post(self, request: Request):
        ser = self.serializer_class(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=ser.data['username'])
        except Exception as e:
            logging.error(e)
            return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUEST)

        if user is None:
            return Response({'error': 'Invalid user'}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(ser.data.get('password')):
            return Response({'error': 'Invalid user'})

        token = RefreshToken.for_user(user)

        return self.success({
            "refresh": str(token),
            "access": str(token.access_token)
        })

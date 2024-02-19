from django.utils.translation import gettext_lazy as _
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from core.enums import Codes, Messages
from core.exceptions import IsBlockException, SmsNotFoundException, \
    IsExpiredException, InvalidConfirmationCodeException
from core.http.models import PendingUser
from core.http.serializers import RegisterSerializer, ConfirmSerializer, \
    ResetPasswordSerializer, \
    ResetConfirmationSerializer, ResendSerializer, UserSerializer
from core.services.BaseService import BaseService
from core.services.sms import SmsService
from core.services.user import UserService
from core.utils.exception import ResponseException
from core.utils.response import ApiResponse


class RegisterView(APIView, BaseService):
    """Register new user"""

    serializer_class = RegisterSerializer
    throttle_classes = [UserRateThrottle]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = UserService()

    def post(self, request: Request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        phone = data.get("phone")
        self.service.create_pending_user(phone, data.get("first_name"),
                                         data.get("last_name"),
                                         data.get("password"))
        self.service.send_confirmation(phone)
        return ApiResponse.success(
            _(Messages.SEND_MESSAGE) % {'phone': phone})


class ConfirmView(APIView, BaseService):
    """Confirm otp code"""

    serializer_class = ConfirmSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = UserService()

    def post(self, request: Request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)

        data = ser.data
        phone = data.get("phone")
        code = data.get("code")

        try:
            pending_user = get_object_or_404(PendingUser, phone=phone)
            if SmsService.check_confirm(phone, code=code):
                token = self.service.create_user_if_not_found(
                    pending_user)
                return ApiResponse.success(_(Messages.OTP_CONFIRMED),
                                           token=token)
        except (
                IsBlockException, SmsNotFoundException,
                IsExpiredException,
                InvalidConfirmationCodeException) as e:
            return ResponseException(e.message)
        except Exception as e:
            return ApiResponse.error(e)


class ResetPasswordView(APIView, BaseService):
    """Reset user password"""
    throttle_classes = [UserRateThrottle]
    serializer_class = ResetPasswordSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = UserService()

    def post(self, request: Request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        phone = ser.data.get('phone')
        self.service.send_confirmation(phone)
        return ApiResponse.success(
            _(Messages.SEND_MESSAGE) % {'phone': phone})


class ResetConfirmationCodeView(APIView, BaseService):
    """Reset confirm otp code"""

    serializer_class = ResetConfirmationSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = UserService()

    def post(self, request: Request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)

        data = ser.data
        code = data.get('code')
        phone = data.get('phone')
        password = data.get('password')

        try:
            res = SmsService.check_confirm(phone, code)
            if res:
                self.service.change_password(phone, password)
                return ApiResponse.success(_(Messages.CHANGED_PASSWORD))
            return ApiResponse.error(_(Messages.INVALID_OTP))
        except (
                IsBlockException, SmsNotFoundException,
                IsExpiredException,
                InvalidConfirmationCodeException) as e:
            return ApiResponse.error(e.message,
                                     error_code=Codes.INVALID_OTP_ERROR)
        except Exception as e:
            return ApiResponse.error(e)


class ResendView(APIView):
    serializer_class = ResendSerializer
    throttle_classes = [UserRateThrottle]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = UserService()

    def post(self, request: Request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        phone = ser.data.get('phone')
        self.service.send_confirmation(phone)
        return ApiResponse.success(
            _(Messages.SEND_MESSAGE) % {'phone': phone})


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user = request.user
        return ApiResponse.success(data=UserSerializer(user).data)

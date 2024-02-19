from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from core.apps.api.v1.auth.views import RegisterView, ConfirmView, \
    ResetPasswordView, ResetConfirmationCodeView, ResendView, MeView

app_name = "auth"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("register/", RegisterView.as_view(), name="register"),
    path("confirm/", ConfirmView.as_view(), name="confirm"),
    path("reset/password/", ResetPasswordView.as_view(),
         name="reset-password"),
    path("confirm/reset/", ResetConfirmationCodeView.as_view(),
         name="reset-confirmation-code"),
    path("resend/", ResendView.as_view(), name="resend"),
    path("me/", MeView.as_view(), name="me"),
]

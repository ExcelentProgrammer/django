from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from core.apps.api.v1.auth.views import (
    RegisterView, ConfirmView,
    ResetPasswordView, ResetConfirmationCodeView,
    ResendView, MeView
)

app_name = "auth"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login view
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token view
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify token
    path("register/", RegisterView.as_view(), name="register"),  # Register
    path("confirm/", ConfirmView.as_view(), name="confirm"),  # Confirm Otp code view
    path("reset/password/", ResetPasswordView.as_view(), name="reset-password"),  # Reset password step 1
    path("confirm/reset/", ResetConfirmationCodeView.as_view(), name="reset-confirmation-code"),
    # Reset password step 2
    path("resend/", ResendView.as_view(), name="resend"),  # resend otp code
    path("me/", MeView.as_view(), name="me"),  # get user information
]

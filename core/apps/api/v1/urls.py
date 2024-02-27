from django.urls import path, include
from rest_framework import routers

from core.apps.api.v1 import views
from core.apps.api.v1.views import FrontendTranslationView

router = routers.DefaultRouter()
router.register("", views.PostListView, basename="posts")

urlpatterns = [
    path("posts/", include(router.urls), name="posts"),
    path("auth/", include("core.apps.api.v1.auth.urls"), name="auth"),
    path("messages/", FrontendTranslationView.as_view(), name="frontend-translation"),
]

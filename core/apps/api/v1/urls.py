from django.urls import path, include
from rest_framework import routers

from core.apps.api.v1 import views

router = routers.DefaultRouter()
router.register("", views.PostListView, basename="posts")

urlpatterns = [
    path("posts/", include(router.urls), name="posts")
]

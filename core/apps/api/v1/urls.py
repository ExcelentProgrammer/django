from django.urls import path

from core.apps.api.v1 import views

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="posts")
]

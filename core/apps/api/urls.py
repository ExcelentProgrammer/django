from django.urls import path, include

urlpatterns = [
    path("v1/", include("core.apps.api.v1.urls"), name="api-v1"),
]

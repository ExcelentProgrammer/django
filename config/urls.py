from django.conf import settings
from django.conf.urls.static import serve
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.apps.home.urls')),
    path("api/", include("core.apps.api.urls")),
    path("rosetta/", include("rosetta.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("debug", include("debug_toolbar.urls")),

    re_path(r"static/(?P<path>.*)", serve, {"document_root": settings.STATIC_ROOT})
]

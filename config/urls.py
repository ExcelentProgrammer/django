from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from config.routes.media import media_urls
from config.routes.swagger import swagger_urls
from core.utils import dd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.apps.home.urls')),
    path("api/", include("core.apps.api.urls")),
    path("rosetta/", include("rosetta.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("debug", include("debug_toolbar.urls")),
]

urlpatterns += media_urls

if settings.DEBUG:
    urlpatterns += swagger_urls

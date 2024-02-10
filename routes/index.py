from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("debug", include("debug_toolbar.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #####################
    # My apps
    #####################
    path("api/", include("core.apps.api.urls")),
    path('', include('core.apps.home.urls')),
]

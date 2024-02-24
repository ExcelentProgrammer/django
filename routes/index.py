from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("i18n/", include("django.conf.urls.i18n")),

    #####################
    # My apps
    #####################
    path("api/", include("core.apps.api.urls")),
    path('', include('core.apps.home.urls')),
]

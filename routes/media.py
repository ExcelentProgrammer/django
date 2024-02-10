#####################
# Static and Media files for production
#####################
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

media_urls = [
    re_path(r"static/(?P<path>.*)", serve, {"document_root": settings.STATIC_ROOT}),
    re_path(r"media/(?P<path>.*)", serve, {"document_root": settings.MEDIA_ROOT}),
]

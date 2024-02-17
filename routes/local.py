from django.urls import path, include

local_urls = [
    path("debug", include("debug_toolbar.urls")),
]

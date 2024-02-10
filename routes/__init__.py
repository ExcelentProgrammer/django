from django.conf import settings

from routes.media import media_urls
from routes.swagger import swagger_urls
from .index import urlpatterns

urlpatterns += media_urls

if settings.DEBUG:
    urlpatterns += swagger_urls

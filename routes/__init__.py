from django.conf import settings

from routes.media import media_urls
from routes.swagger import swagger_urls
from .index import urlpatterns
from .local import local_urls

urlpatterns += media_urls

if settings.DEBUG:
    urlpatterns += swagger_urls
    urlpatterns += local_urls

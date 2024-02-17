from django.conf import settings

from routes.media import media_urls
from .index import urlpatterns

urlpatterns += media_urls

if settings.DEBUG:
    from .local import local_urls
    from routes.swagger import swagger_urls

    urlpatterns += swagger_urls
    urlpatterns += local_urls

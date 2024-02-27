from django.core.cache import cache


class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.cache_timeout = 60

    def __call__(self, request):
        cache_key = f"{request.path}:{request.user.id}"

        if cache.get(cache_key):
            return cache.get(cache_key)

        response = self.get_response(request)
        cache.set(cache_key, response, self.cache_timeout)
        return response

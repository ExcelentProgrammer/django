from django.core.cache import cache


class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.cache_timeout = 60

    def __call__(self, request):
        """
        This function is used to process the incoming request and return the response.

        Args:
            request (HttpRequest): The incoming request object.

        Returns:
            HttpResponse: The response object.
        """
        cache_key = f"{request.path}:{request.user.id}"

        if cache.get(cache_key):
            # Check if the requested data is present in the cache.
            return cache.get(cache_key)

        response = self.get_response(request)

        # Store the response in the cache for the specified time.
        cache.set(cache_key, response, self.cache_timeout)

        return response

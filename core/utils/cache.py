from hashlib import md5

from django.core.cache import cache

from common.env import env


class Cache:

    @staticmethod
    def remember(func, key: str):
        cache_enabled = env('CACHE_ENABLED')
        key = md5(key.encode('utf-8')).hexdigest()
        response = cache.get(key)
        if (response is None) or cache_enabled:
            response = func()
            cache.set(key, response, env("CACHE_TIME"))
        return response

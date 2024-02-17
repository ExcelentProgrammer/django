from hashlib import md5

from django.core.cache import cache

from common.env import env


class Cache:

    @staticmethod
    def remember(func, key=None):
        key = md5(key.encode('utf-8')).hexdigest()
        response = cache.get(key)
        if response is None:
            response = func()
            cache.set(key, response, env("CACHE_TIME"))
        return response

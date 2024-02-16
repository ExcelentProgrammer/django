from .common import *

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
    }
}

MIDDLEWARE += [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ALLOWED_HOSTS += [
    "192.168.100.26",
    "127.0.0.1"
]

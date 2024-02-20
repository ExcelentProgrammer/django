from common.env import env

CACHES = {
    'default': {
        'BACKEND': env("CACHE_BACKEND"),
        'LOCATION': env("CACHE_LOCATION"),
        "TIMEOUT": env("CACHE_TIMEOUT")
    },
}

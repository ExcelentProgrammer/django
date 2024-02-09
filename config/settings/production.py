from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "django",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "localhost",
    }
}

ALLOWED_HOSTS += [
    "192.168.100.26"
]

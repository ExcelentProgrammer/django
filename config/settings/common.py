import importlib
import logging
import os.path
from pathlib import Path

from django.utils.translation import gettext_lazy as _

from common.env import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # har bir parent bitta papka tepaga chiqadi

SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    #####################
    # my install modules
    #####################
    "jazzmin",
    "modeltranslation",

    #####################
    # Default apps
    #####################
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    "corsheaders.middleware.CorsMiddleware",  # Cors middleware
    "django.middleware.locale.LocaleMiddleware",  # Locale middleware for api

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'routes'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "resources/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#####################
# My Settings
#####################
INSTALLED_APPS += [
    "rest_framework",
    "corsheaders",
    "django_filters",
    "rosetta",
    "django_redis",
    "rest_framework_simplejwt",
    "drf_yasg",
    "crispy_forms",
    "import_export",
    "ckeditor",
    "ckeditor_uploader",

    #####################
    # My apps
    #####################
    "core.apps.home.apps.HomeConfig",
    "core.http.HttpConfig",
    "core.apps.api.ApiConfig",
    "core.console.ConsoleConfig",
]

CONFIGS = [
    "config.conf.jazzmin",
    "config.conf.cache",
    "config.conf.ckeditor",
    "config.conf.jwt",
    "config.conf.rest_framework",
]

FACTORYS = [
    ("core.http.factorys.PostFactory", 100),
    ("core.http.factorys.UserFactory", 1),
]

logging.basicConfig(
    filename=f"{BASE_DIR}/logs/django.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "resources/static"),
]

CORS_ORIGIN_ALLOW_ALL = True

STATIC_ROOT = os.path.join(BASE_DIR, "resources/staticfiles")
VITE_APP_DIR = os.path.join(BASE_DIR, "resources/static/vite")

LANGUAGES = (
    ('ru', _('Russia')),
    ('en', _('English')),
    ('uz', _('Uzbek')),
)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale")
]

MODELTRANSLATION_LANGUAGES = ("uz", "ru", "en")
MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"
LANGUAGE_CODE = 'uz'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # Media files

AUTH_USER_MODEL = 'http.User'

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CRISPY_TEMPLATE_PACK = 'tailwind'

#####################
# Import another settings files
#####################
for config in CONFIGS:
    module = importlib.import_module(config)
    for name in dir(module):
        if not name.startswith("__"):
            globals().update({name: getattr(module, name)})

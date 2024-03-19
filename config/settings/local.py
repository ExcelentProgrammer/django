from .common import *
from ..conf.rest_framework import REST_FRAMEWORK

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT":env("DB_PORT"),
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    "core.middlewares.ExceptionMiddleware"
]

####################
# DEBUG BAR
####################
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions"
]

#####################
# Allowed Hosts
#####################
ALLOWED_HOSTS += [
    "127.0.0.1",
    "192.168.100.26"
]

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'user': '10/min',
}

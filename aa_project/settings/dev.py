# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

import os

from aa_project.settings.base import *

DEBUG = True
DJANGO_SETTINGS_MODULE = os.environ['DJANGO_SETTINGS_MODULE']
ALLOWED_HOSTS = ['localhost']

# For Django Debug Toolbar and Django Extensions to be used in dev
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Django Debug Toolbar Settings
INTERNAL_IPS = ['127.0.0.1', '172.24.0.1']

# For Django Debug Toolbar to be used in local dockerized dev environment
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
}

# Additional Middleware
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
]
SHOW_TOOLBAR_CALLBACK = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Do not log static request files to the console
def skip_static_requests(record):
    return not record.args[0].startswith('GET /static/')

# Do not log debug request files to the console
def skip_debug_requests(record):
    return not record.args[0].startswith('GET /__debug__/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'skip_static_requests': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_static_requests,
        },
        'skip_debug_requests': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_debug_requests,
        }
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        'django.server': {
            'level': 'INFO',
            'filters': [
                'skip_static_requests',
                'skip_debug_requests'
            ],
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

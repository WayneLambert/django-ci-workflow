# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

import os

from aa_project.settings.base import *

DEBUG = False
ALLOWED_HOSTS = [os.environ['DIGITAL_OCEAN_IP_ADDRESS']]
DJANGO_SETTINGS_MODULE = os.environ['DJANGO_SETTINGS_MODULE']

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Production settings
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

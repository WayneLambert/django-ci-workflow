# pylint: disable=unused-import
from aa_project.settings.base import SECRET_KEY

# IN-MEMORY TEST DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST': {},
    },
}

PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

from .base import *

DEBUG=False

ALLOWED_HOSTS = ['*']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'database',
            'NAME': 'django',
            'USER': 'django',
            'PASSWORD': 'django',
            'PORT': '3306',
            }
        }

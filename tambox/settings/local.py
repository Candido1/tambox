from .base import *
DEBUG = True
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tambox_desarrollo',
        'USER': 'tambox',
        'PASSWORD': 's0p0rt3ccpp',
        'HOST': 'localhost',
        'PORT': '5432',
        'CHARSET': 'UTF8',
    },
}

LOGIN_URL = '/'
MEDIA_URL = '/media/'
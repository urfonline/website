from .base import *
import dj_database_url
import os


DEBUG = False

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

SECRET_KEY = os.environ['APP_SECRET_KEY']

ALLOWED_HOSTS = ['.herokuapp.com', ]

try:
    from .local import *
except ImportError:
    pass

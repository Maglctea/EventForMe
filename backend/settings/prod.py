from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost:3000', '127.0.0.1:3000', 'localhost:8000', '127.0.0.1:8000', '188.225.24.70']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eventforme',
        'USER': 'postgres',
        'PASSWORD': 'Qwerty12',
        'HOST': 'db',
        'PORT': '5432',
    }
}

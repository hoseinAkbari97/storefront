from .common import *


DEBUG = True

SECRET_KEY =


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'P@ssword',
    }
}

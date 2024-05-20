from .common import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = os.environ.get('DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'P@ssword',
    }
}

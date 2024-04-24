from .common import *

DEBUG=True

ALLOWED_HOSTS = ['0.0.0.0']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'databases/db.sqlite3'),
    }
}

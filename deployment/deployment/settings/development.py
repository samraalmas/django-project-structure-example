from .common import *
import os 


DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0","127.0.0.1"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "databases/db.sqlite3"),
    }
}

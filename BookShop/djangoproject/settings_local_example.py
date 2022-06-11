from pathlib import Path
import os
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False

ALLOWED_HOSTS = ['3.140.249.210']

STATIC_URL = '/static/'
STATIC_FILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DATABASES = {
    'default': {
        'ENGINE': config("DB_ENGINE", default="django.db.backends.sqlite3"),
        'NAME': config("DB_NAME", default=BASE_DIR / "db.sqlite3"),
        "USER": config("DB_USER", default="password"),
        "PASSWORD": config("DB_PASS", default="password"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}
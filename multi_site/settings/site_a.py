from . import *  # noqa


SITE_ID = 1

SECRET_KEY = 'b-awwc8s@1!#i^eb&va&dj5a003a#y(3wiv01^&naj6aj^g6j7'

ALLOWED_HOSTS = [
    '.site-a.example.com',
]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'site-a.sqlite3'),
    }
}

TIME_ZONE = 'Europe/Vilnius'

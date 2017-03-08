from . import *  # noqa


SITE_ID = 2

SECRET_KEY = 'gaa8ub09tl!h(2hwnm5y01%r6$!y-6f+xtw$3j_(f8c5_t++vy'

ALLOWED_HOSTS = [
    '.site-b.example.com',
]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'site-b.sqlite3'),
    }
}

TIME_ZONE = 'Europe/Vilnius'

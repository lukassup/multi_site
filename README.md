# Django multi site setup

Initialize the database tables

```bash
$ DJANGO_SETTINGS_MODULE=multi_site.settings.site_a python manage.py migrate
$ DJANGO_SETTINGS_MODULE=multi_site.settings.site_b python manage.py migrate
```

Run the development server

```bash
$ DJANGO_SETTINGS_MODULE=multi_site.settings.site_a python manage.py runserver site-a.example.com:8000
$ DJANGO_SETTINGS_MODULE=multi_site.settings.site_b python manage.py runserver site-b.example.com:8000
```

Run the WSGI app

```bash
$ gunicorn multi_site.wsgi.site_b
$ gunicorn multi_site.wsgi.site_a
```

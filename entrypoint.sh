#!/bin/sh
cd site_ssplab
python3 manage.py migrate
DJANGO_SUPERUSER_PASSWORD=$ADMIN_PASSWORD python3 manage.py createsuperuser \
    --no-input \
    --username=$ADMIN_USER \
    --email=innovation@insee.fr
gunicorn main.wsgi --bind 0.0.0.0:8000 -w 4
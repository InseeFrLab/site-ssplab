#!/bin/sh
cd site_ssplab
python3 manage.py migrate
# python3 manage.py collectstatic
DJANGO_SUPERUSER_PASSWORD=admin python3 manage.py createsuperuser \
    --no-input \
    --username=admin \
    --email=tom.seimandi@insee.fr
gunicorn main.wsgi --bind 0.0.0.0:8000 -w 4
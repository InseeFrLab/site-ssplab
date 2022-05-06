#!/bin/sh
python3 manage.py migrate
python3 manage.py collectstatic
gunicorn main.wsgi --bind 0.0.0.0:8000 -w 4
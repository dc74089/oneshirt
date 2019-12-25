#!/bin/sh

mkdir -p /etc/app/wewa

./manage.py migrate
./manage.py collectstatic

exec gunicorn --workers 3 --max-requests 30 -b 0.0.0.0:80 oneshirt.wsgi:application

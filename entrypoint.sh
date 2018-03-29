#!/bin/bash

cd /home/ToDoList-Django/server

python manage.py makemigrations
python manage.py migrate

echo Starting Gunicorn.
exec gunicorn -b 0.0.0.0:$DJANGO_PORT server.wsgi

#!/bin/sh

python manage.py flush --no-input
echo "Database flushed successfully"

python3 manage.py migrate
echo "If any required, migrations process has been run"

python3 manage.py collectstatic --no-input --clear
echo "Static files has successfully been collected"

python3 manage.py createsuperuser --no-input

exec "$@"

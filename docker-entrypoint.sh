#!/bin/sh
# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput
# Apply database migrations
# echo "Apply database migrations"
# python ./src/manage.py migrate  --settings=config.settings.local

# Start server

exec "$@"

exec python ./src/manage.py runserver 0.0.0.0:8000 --settings=config.settings.local

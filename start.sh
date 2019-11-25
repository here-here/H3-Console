#!/bin/bash

until nc -z -v -w30 database 3306
do
  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
  sleep 5
done

# PRe-run flush and migrate
python3 manage.py collectstatic
python3 manage.py flush --no-input
python3 manage.py migrate

# Start Gunicorn Process
echo Starting Gunicorn
exec gunicorn h3.wsgi:application \
	--bind 0.0.0.0:8000 \
	--workers 4

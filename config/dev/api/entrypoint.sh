#!/bin/sh

# install all dependencies
pip install -r /dev.txt

# Support sleep for container postgres is up
if [ "$DATABASE" = "dev" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Generate change for structure in database
python manage.py makemigrations
python manage.py migrate

# Copy files static for folder in volume shared by container nginx
python manage.py collectstatic --no-input

# Create log dirs and files
mkdir -p /opt/services/wagtailapp/src/logs
mkdir -p /opt/services/wagtailapp/src/logs/celery

touch /opt/services/wagtailapp/src/logs/celery/celery.schedule-access.log
touch /opt/services/wagtailapp/src/logs/celery/celery.schedule-error.log

touch /opt/services/wagtailapp/src/logs/celery/celery.task-access.log
touch /opt/services/wagtailapp/src/logs/celery/celery.task-error.log


# Start supervisord and services
exec /usr/bin/supervisord -n -c /etc/supervisord.conf
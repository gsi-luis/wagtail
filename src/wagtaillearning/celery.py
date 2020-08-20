from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Establecer las opciones de django para la aplicación de celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wagtaillearning.settings.production')

# Crear la aplicación de Celery
app = Celery('wagtaillearning')

# Especificamos que las variables de configuración de Celery se encuentran
# en el fichero `settings.py` de Django.
# El parámetro namespace es para decir que las variables de configuración de
# Celery en el fichero settings empiezan por el prefijo *CELERY_*
app.config_from_object('django.conf:settings', namespace='CELERY')

# Este método auto-registra las tareas para el broker. 
# Busca tareas dentro de todos los archivos `tasks.py` que haya en las apps
# y las envía a Redis automáticamente.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
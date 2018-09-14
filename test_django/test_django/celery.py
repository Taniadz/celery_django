# countries/celery.py
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django.settings')
app = Celery('test_django')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-data-every-minute': {
        'task': 'countries.tasks.get_dummy_data',
        'schedule': crontab(minute='*/3'),
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
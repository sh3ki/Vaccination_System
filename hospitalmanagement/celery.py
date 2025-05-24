from __future__ import absolute_import, unicode_literals
from datetime import datetime,timedelta
import os
from celery.schedules import schedule
from django import setup
from celery import Celery
from django.conf import settings
from celery.schedules import crontab



os.environ.setdefault('DJANGO_SETTINGS_MODULE','hospitalmanagement.settings')

app = Celery('hospitalmanagement')
app.conf.enable_utc = False

app.conf.update(timezone='Asia\Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')
setup()


from hospital.utils import generate_reminder_dates

CELERY_BEAT_SCHEDULE = generate_reminder_dates()

app.conf.beat_schedule=CELERY_BEAT_SCHEDULE

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"request{self.request !r}")

    

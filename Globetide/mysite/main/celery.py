# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'clear-login-dates-monthly': {
        'task': 'main.tasks.clear_login_dates',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),  # Runs at midnight on the first of every month
    },
}
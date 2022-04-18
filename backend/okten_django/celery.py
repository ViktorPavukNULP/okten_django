import os

from celery import Celery
# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'okten_django.settings')

app = Celery('okten_django')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_spam_every_month": {
        'task': 'tasks.spam.spam_email',
        'schedule': crontab(minute='0', hour='18', day_of_month='15')
    }
}

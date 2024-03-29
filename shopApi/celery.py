import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'shopApi.settings'
)

app = Celery('shopApi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery spam tasks
app.conf.beat_schedule = {
    'send-spam-every-5minutes': {
        'task': 'shopApi.tasks.send_spam_email',
        'schedule': crontab()
    }
}

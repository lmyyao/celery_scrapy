CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 1

# CELERYBEAT_SCHEDULE = {
#     'add-every-30-seconds': {
#         'task': 'proj.tasks.add',
#         'schedule': timedelta(seconds=30),
#         'args': (16, 16)
#     },
# }

from kombu import Exchange, Queue

CELERY_ROUTES = {'proj.tasks.add': {'routing_key': 'default', "exchange": "default"}}
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue("lmy", Exchange("default"), routing_key="lmy"),
)

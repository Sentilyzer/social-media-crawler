BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True


from datetime import timedelta

CELERYBEAT_SCHEDULE = \
{
    'query-every-hour':
    {
        'task': 'WaterSupplyMonitor.QueryWaterCutInfo',
        'schedule': timedelta(seconds=30),
        'args': ()
    },
}

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
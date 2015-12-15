from datetime import timedelta

CELERYBEAT_SCHEDULE = \
{
    'query-every-hour':
    {
        'task': 'WaterSupplyMonitor.QueryWaterCutInfo',
        'schedule': timedelta(seconds=3600),
        'args': ()
    },
}

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
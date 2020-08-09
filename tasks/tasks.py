from celery import Celery

import config.CeleryConfig as celeryConfig
import datetime

from tasks.rest_check.restCheck import call_api

app = Celery('apiHealth')
app.config_from_object(celeryConfig)


@app.task
def heart_beat():
    print('------ celery is alive')
    return datetime.datetime.today()

@app.task
def api_reach(url, method, timeout):
    res = call_api(url, method, timeout)
    if res['status'] == 0:
        print(f'------{res["status"]["result"]}0')
    else:
        print('error handling')


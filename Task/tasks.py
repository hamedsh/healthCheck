from celery import Celery

import datetime
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/Task/')

import celeryConfig
from rest_check.restCheck import call_api

app = Celery('apiHealth')
app.config_from_object(celeryConfig)


@app.task
def heart_beat():
    print('------ celery is alive')
    return datetime.datetime.today()


@app.task
def api_reach(url, method, timeout, body):
    res = call_api(url, method, timeout, body)
    if res['status'] == 0:
        print(f'------{res["result"]}')
    else:
        print('error handling'+ str(res))


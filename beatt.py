import tasks
from celeryConfig import redbeat_key_prefix
from db.Service import Service
from redbeat import RedBeatSchedulerEntry as Entry
from db.dbConnector import HealthCheckDB, SQLITE
from beat import Beater

BASE_KEY = 'beater_{}'

db = HealthCheckDB(SQLITE, dbname='db/healthcheck.db')
beater = Beater()

services = db.get_services()
# beater.check_tasks(services)
# for service_ in services:
#     service = Service(service_)
#     # try:
#     #     entry = Entry.from_key(redbeat_key_prefix + BASE_KEY.format(service.name), app=tasks.app)
#     # #     todo: check entry existence
#     # except:
#     if service.type == 1:
#         # entry = Entry(BASE_KEY.format(service.name), f'tasks.{service.type_name}', service.repeat_period,
#         #           args=[service.metadata['url'], service.metadata['method'],
#         #                 service.metadata['timeout'], service.metadata.get('body', None)],
#         #               app=tasks.app)
entry = Entry(f'urlCheck_1', 'tasks.heart_beat', 5, app=tasks.app)
entry.save()
print(entry.key)

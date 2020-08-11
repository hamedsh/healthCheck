from redbeat import RedBeatSchedulerEntry as Entry

from Task import tasks
from db.Service import Service
from Task.celeryConfig import redbeat_key_prefix

BASE_KEY = 'beater_{}'

class Beater:
    def check_tasks(self, services: list, create: bool = True):
        for service_ in services:
            service = Service(service_)
            try:
                entry = Entry.from_key(redbeat_key_prefix + BASE_KEY.format(service.name), app=tasks.app)
            #     todo: check entry existence
            except:
                if create:
                    if service.type == 1:
                        entry = Entry(BASE_KEY.format(service.name), f'tasks.{service.type_name}', service.repeat_period,
                                  args=[service.metadata['url'], service.metadata['method'],
                                        service.metadata['timeout'], service.metadata.get('body', None)],
                                      app=tasks.app)
                        entry.save()
                        print(entry.key)
        return 0

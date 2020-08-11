import yaml
import os
config_path = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])
# config_path = os.path.dirname(os.path.abspath(__file__))

with open(f'{config_path}/config/config.yml') as config_file:
    configs = yaml.load(config_file, Loader=yaml.FullLoader)

broker_url = f'redis://{configs["celery_config"]["redis_address"]}:{configs["celery_config"]["redis_port"]}/10'
redbeat_redis_url = f'redis://{configs["celery_config"]["redis_address"]}:{configs["celery_config"]["redis_port"]}/11'

beat_scheduler = 'redbeat.RedBeatScheduler'

beat_max_loop_interval = 5
redbeat_key_prefix = 'redbeat_'

# beat_schedule = {
#     'check_heartbeat_every_5_second': {
#         'task': 'tasks.heart_beat',
#         'schedule': 5.0,
#         'name': '_heartbeat'
#     }
# }

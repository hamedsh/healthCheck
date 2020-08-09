import yaml

with open('config/config.yml') as config_file:
    configs = yaml.load(config_file, Loader=yaml.FullLoader)

with configs["celery_config"] as celery_config:
    broker_url = f'redis://{celery_config["redis_address"]}:{celery_config["redis_port"]}/10'
    redbeat_redis_url = f'redis://{celery_config["redis_address"]}:{celery_config["redis_port"]}/11'

beat_max_loop_interval = 5
redbeat_key_prefix = 'redbeat'

beat_schedule = {
    'check_heartbeat_every_5_second': {
        'task': 'tasks.heartBeat',
        'schedule': 5.0,
        'name': '_heartbeat'
    }
}

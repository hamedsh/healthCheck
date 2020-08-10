import json
class Service(object):
    id: int = None
    name: str = None
    type: int = None
    type_name: str = None
    repeat_period: int = 5     # repeat period by second
    metadata = {}

    def __init__(self, arr: list):
        self.id = arr[0]
        self.name = arr[1]
        self.type = arr[2]
        self.type_name = arr[3]
        self.repeat_period = arr[4]
        self.metadata = json.loads(arr[5].replace("'", '"'))

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

from db.queries import QUERIES

SQLITE = 'sqlite'

SERVICES = 'services'
TASKS = 'tasks'
SERVICE_TYPES = 'service_types'
SERVICE_STATUS = 'service_status'


class HealthCheckDB:
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }
    db_engine = None

    def __init__(self, dbtype: str, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            try:
                engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
                self.db_engine = create_engine(engine_url)
            except Exception as e:
                raise Exception(e)
        else:
            raise Exception('unknown db type')

    def create_db_tables(self):
        metadata = MetaData()
        services = Table(SERVICES, metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String, unique=True, nullable=False),
                         Column('type', Integer, ForeignKey(f'{SERVICE_TYPES}.id'), nullable=False),
                         Column('metadata', String, nullable=False),
                         Column('status', Integer, ForeignKey(f'{SERVICE_STATUS}.id'), nullable=False)
                         )
        tasks = Table(TASKS, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('service_id', Integer, ForeignKey(f'{SERVICES}.id')),
                      Column('key', String, nullable=False)
                      )
        service_type = Table(SERVICE_TYPES, metadata,
                             Column('id', Integer, primary_key=True),
                             Column('Type', String),
                             )
        service_status = Table(SERVICE_STATUS, metadata,
                             Column('id', Integer, primary_key=True),
                             Column('state', String),
                             )
        try:
            metadata.create_all(self.db_engine)
        except Exception as e:
            return -1, e.__str__()
        return 0, ''

    def execute_query(self, query):
        if query == '': return 0
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                return -1, e.__str__()
        return 0

    def add_service(self, name, type: int, metadata):
        queries = QUERIES['add_service'].format()


#     todo: db initialize

a= HealthCheckDB(SQLITE, dbname='healthcheck.db')
a.create_db_tables()




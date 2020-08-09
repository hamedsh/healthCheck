from flask import Flask, jsonify
from db.dbConnector import HealthCheckDB, SQLITE
from tasks.beat import Beater

app = Flask(__name__)


@app.route('/get_services')
def get_services():
    global db
    a = db.get_services()
    return a.__str__()


if __name__ == '__main__':
    db = HealthCheckDB(SQLITE, dbname='db/healthcheck.db')
    beater = Beater()

    services = db.get_services()
    beater.check_tasks(services)
    app.run()

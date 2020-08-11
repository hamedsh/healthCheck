from random import randint
from time import sleep

from flask import Flask, jsonify, request

# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
from kombu.utils import json

app = Flask("test")


@app.route("/error504", methods=["GET", "POST"])
def funcerr504():
    return jsonify({"error": "error type message"}), 504


@app.route("/error503", methods=["GET", "POST"])
def funcerr503():
    return jsonify({"error": "error type message"}), 503


@app.route("/ok", methods=["GET", "POST"])
def funcOk():
    if request.method == 'GET':
        num = request.args.get('num', '0')
    else:
        print(request.data)
        num = json.loads(request.data)['num']
    sleep(randint(2, 5))
    return jsonify({"message": "OK message", "val": int(num) * 9}), 200


app.run('0.0.0.0', 8008, debug=False)

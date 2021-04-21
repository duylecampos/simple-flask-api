from flask import Flask, jsonify, request, abort
from src import database
from src.entities import Event
from src.exceptions import AccountNotFound, UnknownEvent
from src.repositories import AccountRepository
from src.processors.factory import factory


app = Flask(__name__)


@app.route("/reset", methods=["POST"])
def reset():
    database.reset()
    return "OK", 200


@app.route("/event", methods=["POST"])
def exec_event():
    request_data = request.get_json(force=True)
    try:
        event = Event(**request_data)
    except TypeError:
        return "Invalid arguments", 400

    try:
        processor = factory(event, database)
        event_result = processor.exec(event)
        return jsonify(event_result), 201
    except AccountNotFound:
        return "0", 404
    except UnknownEvent as e:
        return str(e), 400


@app.route("/balance", methods=["GET"])
def balance():
    account_id = request.args.get("account_id")
    account = AccountRepository(database).find(account_id)
    if not account:
        return "0", 404
    return str(account.balance), 200

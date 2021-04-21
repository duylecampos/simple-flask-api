from flask import Flask, jsonify, request, abort
from src import database
from src.entities import Event
from src.exceptions import AccountNotFound
from src.repositories import AccountRepository


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

    account_repository = AccountRepository(database)
    try:
        if event.type == "deposit":
            destination = account_repository.deposit(event)
            return jsonify({"destination": destination}), 201
        elif event.type == "withdraw":
            origin = account_repository.withdraw(event)
            return jsonify({"origin": origin}), 201
        elif event.type == "transfer":
            origin, destination = account_repository.transfer(event)
            return jsonify({"origin": origin, "destination": destination}), 201
        else:
            return "Invalid event type!", 400
    except AccountNotFound:
        return "0", 404
    return jsonify({"destination": account}), 201


@app.route("/balance", methods=["GET"])
def balance():
    account_id = request.args.get("account_id")
    account_repository = AccountRepository(database)
    account = account_repository.find(account_id)
    if not account:
        return "0", 404
    return str(account.balance), 200

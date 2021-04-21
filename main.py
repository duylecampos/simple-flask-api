from flask import Flask, jsonify, request, abort
from src import database
from src.entities import Event
from src.repositories import AccountRepository


app = Flask(__name__)

@app.route('/reset', methods=['POST'])
def reset():
    database.reset()
    return 'OK', 200

@app.route('/event', methods=['POST'])
def exec_event():
    request_data = request.get_json()
    try:
        event = Event(**request_data)
    except TypeError:
        abort(400, 'Invalid arguments')
    
    account_repository = AccountRepository(database)
    try:
        if event.type == 'deposit':
    account = account_repository.deposit(event)
        elif event.type == 'withdraw':
            account = account_repository.withdraw(event)
        else:
            return 'Invalid event type!', 400
    except AccountNotFound:
        return '0', 404
    return jsonify({'destination': account}), 201

    

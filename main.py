from flask import Flask, jsonify, request, abort
from src import database
from src.entities import Event
from src.repositories import AccountRepository


app = Flask(__name__)

@app.route('/event', methods=['POST'])
def exec_event():
    request_data = request.get_json()
    try:
        event = Event(**request_data)
    except TypeError:
        abort(400, 'Invalid arguments')
    
    account_repository = AccountRepository(database)
    account = account_repository.deposit(event)

    return jsonify({'destination': account}), 201

    

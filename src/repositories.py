from typing import Tuple
from src import database
from src.entities import Event, Account
from src.exceptions import AccountNotFound


class AccountRepository:

    _database = None

    def __init__(self, database):
        self._database = database

    def find(self, account_id: str) -> Account:
        return self._database.find(account_id)

    def deposit(self, event: Event) -> Account:
        account = self.find(event.destination)
        if not account:
            account = Account(id=event.destination)
        account.deposit(event.amount)
        self._database.upsert(account)
        return account

    def withdraw(self, event: Event) -> Account:
        account = self.find(event.origin)
        if not account:
            raise AccountNotFound()
        account.withdraw(event.amount)
        self._database.upsert(account)
        return account

    def transfer(self, event: Event) -> Tuple[Account, Account]:
        origin = self.withdraw(event)
        destination = self.deposit(event)
        return (origin, destination)

from src.processors.base import BaseProcessor
from src.entities import Event, Account


class DepositProcessor(BaseProcessor):
    def _format_output(self, account: Account):
        return {"destination": account}

    def exec(self, event: Event):
        account = self._account_repository.deposit(event)
        return self._format_output(account)

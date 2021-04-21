from src.processors.base import BaseProcessor
from src.entities import Event, Account


class WithdrawProcessor(BaseProcessor):
    def _format_output(self, account: Account):
        return {"origin": account}

    def exec(self, event: Event):
        account = self._account_repository.withdraw(event)
        return self._format_output(account)
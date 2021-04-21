from src.processors.base import BaseProcessor
from src.entities import Event, Account


class TransferProcessor(BaseProcessor):
    def _format_output(self, origin: Account, destination: Account):
        return {"origin": origin, "destination": destination}

    def exec(self, event: Event):
        origin, destination = self._account_repository.transfer(event)
        return self._format_output(origin, destination)
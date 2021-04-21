from src.entities import Event
from src.exceptions import UnknownEvent
from src.processors.deposit import DepositProcessor
from src.processors.withdraw import WithdrawProcessor
from src.processors.transfer import TransferProcessor


def factory(event: Event, database):
    if event.type == "deposit":
        return DepositProcessor(database)
    elif event.type == "withdraw":
        return WithdrawProcessor(database)
    elif event.type == "transfer":
        return TransferProcessor(database)
    else:
        raise UnknownEvent(f"Event of type {event.type} isn't known!")

from abc import ABC, abstractmethod
from typing import Dict
from src.entities import Event, Account
from src.repositories import AccountRepository


class BaseProcessor(ABC):

    _account_repository = None

    def __init__(self, database):
        self._account_repository = AccountRepository(database)

    @abstractmethod
    def _format_output(self, **kwargs) -> Dict[str, Account]:
        pass

    @abstractmethod
    def exec(self, event: Event):
        pass
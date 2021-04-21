from dataclasses import dataclass
from typing import Optional

@dataclass
class Account:
    id: str
    balance: float = 0.0 

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

@dataclass
class Event:
    type: str
    amount: float
    origin: Optional[str] = None
    destination: Optional[str] = None

    def __post_init__(self):
        if not self.origin and not self.destination:
            raise TypeError('One of destination and origin must exist!')
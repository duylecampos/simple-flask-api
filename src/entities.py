from dataclasses import dataclass

@dataclass
class Account:
    id: str
    balance: float = 0.0 

    def deposit(self, amount: float):
        self.balance += amount

@dataclass
class Event:
    type: str
    destination: Account
    amount: float
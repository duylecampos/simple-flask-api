from src.entities import Account

storage = {}

def reset():
    global storage
    storage = {}

def find(id: str) -> Account:
    return storage.get(id)

def upsert(account: Account) -> Account:
    storage[account.id] = account
    return account
    
    
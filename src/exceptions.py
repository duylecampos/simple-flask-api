class AccountNotFound(Exception):
    """Raise when the account number can not be found"""

    pass


class UnknownEvent(Exception):
    """Raise when unknown event is sent"""
    pass
class InsufficientAmountError(Exception):
    pass


class Wallet:

    def __init__(self, amount=0):
        self._balance = amount  # protected

    def _validate_operation(self, spending):
        if self._balance < spending:
            raise InsufficientAmountError

    def add_cash(self, cash):
        self._balance += cash

    def spend_cash(self, spending):
        self._validate_operation(spending=spending)
        self._balance -= spending

    def get_balance(self):
        return self._balance

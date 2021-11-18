class InsufficientAmount(Exception):
    pass


class Wallet:

    def __init__(self, amount=0):
        self.balance = 0  # public
        self._balance = 0  # protected
        self.__balance = 0  # protected

    def _validate_operation(self, spending):
        pass

    def add_cash(self, cash):
        pass

    def spend_cash(self, spending):
        pass

    def get_balance(self):
        pass

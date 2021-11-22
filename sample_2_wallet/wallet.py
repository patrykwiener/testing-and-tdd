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


if __name__ == '__main__':
    wallet = Wallet(amount=10)
    print(wallet.get_balance())
    wallet.add_cash(cash=10)
    print(wallet.get_balance())
    wallet.spend_cash(spending=10)
    print(wallet.get_balance())
    wallet.spend_cash(spending=20)
    print(wallet.get_balance())

    empty_wallet = Wallet()
    t = 0


from sample_5_mocks.wallet import Wallet


class Owner:

    def __init__(self, first_name, last_name, wallet: Wallet):
        pass

    def supply_wallet(self, cash):
        pass

    def withdraw_money(self, amount):
        pass

    def check_if_can_afford(self, amount):
        pass


if __name__ == '__main__':
    wallet = Wallet()
    owner = Owner(first_name='Ala', last_name='Makota', wallet=wallet)

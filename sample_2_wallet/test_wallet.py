import pytest

from sample_2_wallet.wallet import Wallet, InsufficientAmountError


class TestWallet:

    def test_default_initial_amount(self):
        wallet = Wallet()
        expected = 0

        actual = wallet.get_balance()

        assert expected == actual

    def test_setting_initial_amount(self):
        amount = 10
        wallet = Wallet(amount=amount)
        expected = 10

        actual = wallet.get_balance()

        assert expected == actual

    def test_spend_cash(self):
        amount = 10
        wallet = Wallet(amount=amount)
        spending = 10
        expected = 0

        wallet.spend_cash(spending=spending)
        actual = wallet.get_balance()

        assert expected == actual

    def test_add_cash(self):
        amount = 10
        wallet = Wallet(amount=amount)
        cash = 10
        expected = 20

        wallet.add_cash(cash=cash)
        actual = wallet.get_balance()

        assert expected == actual

    def test_spend_cash_raises_exception_on_insufficient_amount(self):
        wallet = Wallet()
        spending = 10
        with pytest.raises(InsufficientAmountError):
            wallet.spend_cash(spending=spending)

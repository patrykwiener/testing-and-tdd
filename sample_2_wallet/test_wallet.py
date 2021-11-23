import pytest

from sample_2_wallet.wallet import Wallet, InsufficientAmountError


class TestWallet:
    AMOUNT = 10
    SPENDING = 10

    def setup_method(self):
        self.wallet = Wallet(amount=self.AMOUNT)
        self.empty_wallet = Wallet()

    def test_default_initial_amount(self):
        expected = 0

        actual = self.empty_wallet.get_balance()

        assert expected == actual

    def test_setting_initial_amount(self):
        actual = self.wallet.get_balance()

        assert self.AMOUNT == actual

    def test_spend_cash(self):
        expected = 0

        self.wallet.spend_cash(spending=self.SPENDING)
        actual = self.wallet.get_balance()

        assert expected == actual

    def test_add_cash(self):
        cash = 10
        expected = 20

        self.wallet.add_cash(cash=cash)
        actual = self.wallet.get_balance()

        assert expected == actual

    def test_spend_cash_raises_exception_on_insufficient_amount(self):
        with pytest.raises(InsufficientAmountError):
            self.empty_wallet.spend_cash(spending=self.SPENDING)

    @pytest.mark.parametrize(
        'cash,spending,expected',
        [
            [20, 10, 10],
            [10, 10, 0],
            [0, 0, 0],
        ]
    )
    def test_wallet_transaction(self, cash, spending, expected):
        """
        add_cash
        spend_cash
        assert
        """
        self.empty_wallet.add_cash(cash=cash)
        self.empty_wallet.spend_cash(spending=spending)
        result = self.empty_wallet.get_balance()

        assert expected == result

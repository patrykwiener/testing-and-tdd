from unittest.mock import MagicMock

import pytest

from sample_5_mocks.owner import Owner
from sample_5_mocks.wallet import InsufficientAmountError


class TestOwner:
    FIRST_NAME = 'test_name'
    LAST_NAME = 'test_surname'

    def setup_method(self) -> None:
        self.wallet_mock = MagicMock()  # == Wallet()
        self.owner = Owner(first_name=self.FIRST_NAME, last_name=self.LAST_NAME, wallet=self.wallet_mock)

    def test_owner_first_name(self):
        assert self.owner.first_name == self.FIRST_NAME

    def test_owner_last_name(self):
        assert self.owner.last_name == self.LAST_NAME

    def test_owner_supply_to_wallet(self):
        cash = 10

        self.owner.supply_wallet(cash=cash)

        self.wallet_mock.add_cash.assert_called_once_with(cash=cash)

    def test_owner_withdraw_money(self):
        amount = 10

        self.owner.withdraw_money(amount=amount)

        self.wallet_mock.spend_cash.assert_called_once_with(spending=amount)

    def test_owner_check_if_can_afford_true(self):
        amount = 10
        self.wallet_mock.get_balance.return_value = 20
        # self.wallet_mock.get_balance = MagicMock(return_value=20)

        result = self.owner.check_if_can_afford(amount=amount)

        # assert result is True
        assert result
        self.wallet_mock.get_balance.assert_called_once()

    def test_owner_check_if_can_afford_false(self):
        amount = 30
        self.wallet_mock.get_balance.return_value = 20
        # self.wallet_mock.get_balance = MagicMock(return_value=20)

        result = self.owner.check_if_can_afford(amount=amount)

        # assert result is False
        assert not result
        self.wallet_mock.get_balance.assert_called_once()

    def test_owner_withdraw_money_raises_exception(self):
        amount = 10
        # self.wallet_mock.spend_cash = MagicMock(side_effect=InsufficientAmountError)
        self.wallet_mock.spend_cash.side_effect = InsufficientAmountError

        with pytest.raises(InsufficientAmountError):
            self.owner.withdraw_money(amount=amount)

        self.wallet_mock.spend_cash.assert_called_once_with(spending=amount)

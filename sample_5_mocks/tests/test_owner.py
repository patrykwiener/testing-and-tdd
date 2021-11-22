from unittest.mock import MagicMock

from sample_5_mocks.owner import Owner


class TestOwner:
    FIRST_NAME = 'test_name'
    LAST_NAME = 'test_surname'

    def setup_method(self) -> None:
        self.wallet_mock = MagicMock()  # == Wallet()
        self.owner = Owner(self.FIRST_NAME, self.LAST_NAME, self.wallet_mock)

    def test_owner_first_name(self):
        pass

    def test_owner_last_name(self):
        pass

    def test_owner_supply_to_wallet(self):
        pass

    def test_owner_withdraw_money(self):
        pass

    def test_owner_check_if_can_afford_true(self):
        pass

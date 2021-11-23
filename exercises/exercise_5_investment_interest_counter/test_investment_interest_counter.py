import pytest

from exercises.exercise_5_investment_interest_counter.investment_interest_counter import InvestmentInterestCounter


class TestInvestmentInterestCounter:
    INTEREST_RATE = 0.01
    BALANCE = 10000

    def setup_method(self) -> None:
        self.account = InvestmentInterestCounter(self.INTEREST_RATE, self.BALANCE)

    @pytest.mark.parametrize('duration, expected_balance', [
        [0, 10000],
        [1, 10100],
        [2, 10201]])
    def test_yearly_capitalization(self, duration, expected_balance):
        pass

    def test_yearly_capitalization_raises_exception(self):
        pass

from gdb.domain.account import Account
from gdb.exceptions import InvalidAmountException


class SavingsAccount(Account):
    def __init__(self, account_number, name, age, balance, status="Active", interest_rate=4.0):
        self._interest_rate = interest_rate
        super().__init__(account_number, name, age, balance, "Savings", status)
        if balance < self.get_minimum_balance():
            raise InvalidAmountException("Balance below minimum required for SavingsAccount")

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value

    def get_minimum_balance(self) -> float:
        return 500.0

    def calculate_interest(self) -> float:
        return (self._balance * self._interest_rate) / 100.0

    def add_interest(self) -> float:
        interest = self.calculate_interest()
        self._balance += interest
        return interest

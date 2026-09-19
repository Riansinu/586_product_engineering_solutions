from gdb.domain.account import Account


class CurrentAccount(Account):
    def __init__(self, account_number, name, age, balance, status="Active", overdraft_limit=10000.0):
        self._overdraft_limit = overdraft_limit
        super().__init__(account_number, name, age, balance, "Current", status)

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, value):
        self._overdraft_limit = value

    def get_minimum_balance(self) -> float:
        limit = getattr(self, "_overdraft_limit", 10000.0)
        return -limit

    def calculate_interest(self) -> float:
        return 0.0

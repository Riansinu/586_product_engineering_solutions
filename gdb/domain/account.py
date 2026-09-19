from gdb.domain.bank_account import BankAccount


class Account(BankAccount):
    def __init__(self, account_number, name, age, balance, account_type, status="Active"):
        super().__init__(account_number, name, age, balance, account_type, status)
        min_bal = self.get_minimum_balance()
        if balance < min_bal:
            from gdb.exceptions import InvalidAmountException
            raise InvalidAmountException("Balance below minimum requirement")

    def get_minimum_balance(self) -> float:
        return 500.0 if self._account_type == "Savings" else 1000.0

    def calculate_interest(self) -> float:
        return 0.0

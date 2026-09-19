from gdb.domain.i_account import IAccount
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.salary_account import SalaryAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.exceptions import InvalidAccountDataException


class AccountFactory:
    @staticmethod
    def create_account(account_type: str, account_number, name, age, balance, status="Active", **kwargs) -> IAccount:
        acc_type = account_type.upper().replace("_", "").replace(" ", "")

        if acc_type == "SAVINGS":
            return SavingsAccount(account_number, name, age, balance, status, **kwargs)
        elif acc_type == "CURRENT":
            return CurrentAccount(account_number, name, age, balance, status, **kwargs)
        elif acc_type == "SALARY":
            return SalaryAccount(account_number, name, age, balance, status, **kwargs)
        elif acc_type in ("FIXEDDEPOSIT", "FD"):
            return FixedDepositAccount(account_number, name, age, balance, status, **kwargs)
        else:
            raise InvalidAccountDataException(f"Invalid account type: {account_type}")

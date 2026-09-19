from gdb.domain.bank_account import BankAccount
from gdb.domain.i_account import IAccount


class AbstractAccount(BankAccount, IAccount):
    def __init__(self, account_number, name, age, balance, account_type, status="Active"):
        super().__init__(account_number, name, age, balance, account_type, status)

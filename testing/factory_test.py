from gdb.factory import AccountFactory
from gdb.domain import IAccount, SavingsAccount, CurrentAccount, SalaryAccount, FixedDepositAccount


def test_factory():
    sav = AccountFactory.create_account("SAVINGS", "S101", "Alice", 25, 2000.0)
    cur = AccountFactory.create_account("CURRENT", "C101", "Bob", 30, 5000.0)
    sal = AccountFactory.create_account("SALARY", "SAL101", "Charlie", 28, 1000.0)
    fd = AccountFactory.create_account("FIXEDDEPOSIT", "FD101", "David", 40, 10000.0)

    assert isinstance(sav, IAccount)
    assert isinstance(cur, IAccount)
    assert isinstance(sal, IAccount)
    assert isinstance(fd, IAccount)

    assert isinstance(sav, SavingsAccount)
    assert isinstance(cur, CurrentAccount)
    assert isinstance(sal, SalaryAccount)
    assert isinstance(fd, FixedDepositAccount)

    accounts = [sav, cur, sal, fd]
    for acc in accounts:
        acc.deposit(500.0)
        assert acc.balance > 0
        min_bal = acc.get_minimum_balance()
        assert min_bal is not None
        interest = acc.calculate_interest()
        assert interest >= 0
        acc.display_account_info()


if __name__ == "__main__":
    test_factory()

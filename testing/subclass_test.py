from gdb.domain import Account, SavingsAccount, CurrentAccount
from gdb.exceptions import InsufficientBalanceException


def test_subclasses():
    sav = SavingsAccount("SAV101", "Alice", 30, 1000.0, interest_rate=4.0)
    assert sav.account_type == "Savings"
    assert sav.interest_rate == 4.0

    interest = sav.calculate_interest()
    assert interest == 40.0

    added = sav.add_interest()
    assert added == 40.0
    assert sav.balance == 1040.0

    try:
        sav.withdraw(600.0)
        assert False, "Should have raised InsufficientBalanceException"
    except InsufficientBalanceException:
        pass

    cur = CurrentAccount("CUR202", "Bob", 35, 1000.0, overdraft_limit=5000.0)
    assert cur.account_type == "Current"
    assert cur.overdraft_limit == 5000.0

    assert cur.withdraw(3000.0) is True
    assert cur.balance == -2000.0

    try:
        cur.withdraw(4000.0)
        assert False, "Should have raised InsufficientBalanceException"
    except InsufficientBalanceException:
        pass

    accounts = [
        SavingsAccount("SAV1", "Alice", 25, 2000.0),
        CurrentAccount("CUR1", "Bob", 30, 3000.0),
    ]

    for acc in accounts:
        assert isinstance(acc, Account)
        acc.deposit(500.0)
        acc.display_account_info()


if __name__ == "__main__":
    test_subclasses()

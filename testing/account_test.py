from gdb.domain import Account, BankAccount
from gdb.exceptions import InvalidAmountException, InsufficientBalanceException


def test_account():
    acc = Account("ACC123", "John Doe", 25, 1000.0, "Savings")

    assert acc.account_number == "ACC123"
    assert acc.name == "John Doe"
    assert acc.age == 25
    assert acc.balance == 1000.0
    assert acc.account_type == "Savings"
    assert acc.status == "Active"

    acc.name = "Jane Doe"
    assert acc.name == "Jane Doe"

    assert acc.deposit(500.0) is True
    assert acc.balance == 1500.0

    try:
        res = acc.deposit(-100.0)
        assert res is False
    except InvalidAmountException:
        pass
    assert acc.balance == 1500.0

    assert acc.withdraw(200.0) is True
    assert acc.balance == 1300.0

    try:
        res = acc.withdraw(2000.0)
        assert res is False
    except (InsufficientBalanceException, InvalidAmountException):
        pass
    assert acc.balance == 1300.0

    acc.display_account_info()


if __name__ == "__main__":
    test_account()

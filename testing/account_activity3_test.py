from gdb.domain import Account, BankAccount
from gdb.exceptions import (
    InvalidAmountException,
    InsufficientBalanceException,
    InvalidPinException,
    AccountInactiveException,
    InvalidAccountDataException,
)


def test_activity3():
    try:
        acc1 = Account("ACC1", "Young User", 15, 200.0, "Savings")
    except (InvalidAccountDataException, InvalidAmountException):
        acc1 = None

    acc2 = Account("ACC2", "Adult User", 30, 2000.0, "Current")
    assert acc2.age == 30
    assert acc2.balance == 2000.0

    assert acc2.has_pin() is False
    try:
        res = acc2.set_pin(12)
        assert res is False
    except InvalidPinException:
        pass

    assert acc2.set_pin(1234) is True
    assert acc2.has_pin() is True
    assert acc2.verify_pin(1234) is True
    assert acc2.verify_pin(9999) is False

    try:
        res = acc2.withdraw(500.0, 9999)
        assert res is False
    except InvalidPinException:
        pass

    assert acc2.withdraw(500.0, 1234) is True
    assert acc2.balance == 1500.0

    try:
        res = acc2.withdraw(10000.0, 1234)
        assert res is False
    except InsufficientBalanceException:
        pass

    assert acc2.close_account() is True
    assert acc2.status == "Inactive"

    try:
        res = acc2.deposit(100.0)
        assert res is False
    except AccountInactiveException:
        pass

    try:
        res = acc2.withdraw(100.0, 1234)
        assert res is False
    except AccountInactiveException:
        pass

    assert acc2.reopen_account() is True
    assert acc2.status == "Active"
    assert acc2.deposit(100.0) is True
    assert acc2.balance == 1600.0


if __name__ == "__main__":
    test_activity3()

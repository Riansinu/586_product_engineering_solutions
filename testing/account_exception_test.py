from gdb.domain.account import Account
from gdb.exceptions import (
    InvalidAmountException,
    InsufficientBalanceException,
    InvalidPinException,
    AccountInactiveException,
    InvalidAccountDataException,
)


def test_exceptions():
    try:
        Account("ACC1", "Minor", 16, 1000.0, "Savings")
        assert False, "Should have raised InvalidAccountDataException"
    except InvalidAccountDataException:
        pass

    try:
        Account("ACC2", "Adult", 25, 100.0, "Savings")
        assert False, "Should have raised InvalidAmountException"
    except InvalidAmountException:
        pass

    acc = Account("ACC3", "Valid User", 25, 2000.0, "Savings")

    try:
        acc.deposit(-50.0)
        assert False, "Should have raised InvalidAmountException"
    except InvalidAmountException:
        pass

    try:
        acc.withdraw(-50.0)
        assert False, "Should have raised InvalidAmountException"
    except InvalidAmountException:
        pass

    try:
        acc.set_pin("12")
        assert False, "Should have raised InvalidPinException"
    except InvalidPinException:
        pass

    acc.set_pin(1234)

    try:
        acc.withdraw(100.0, 9999)
        assert False, "Should have raised InvalidPinException"
    except InvalidPinException:
        pass

    try:
        acc.withdraw(1800.0, 1234)
        assert False, "Should have raised InsufficientBalanceException"
    except InsufficientBalanceException:
        pass

    acc.close_account()

    try:
        acc.deposit(100.0)
        assert False, "Should have raised AccountInactiveException"
    except AccountInactiveException:
        pass

    try:
        acc.withdraw(100.0, 1234)
        assert False, "Should have raised AccountInactiveException"
    except AccountInactiveException:
        pass


if __name__ == "__main__":
    test_exceptions()

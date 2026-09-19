class AccountException(Exception):
    pass


class InvalidAmountException(AccountException):
    pass


class InsufficientBalanceException(AccountException):
    pass


class InvalidPinException(AccountException):
    pass


class AccountInactiveException(AccountException):
    pass


class InvalidAccountDataException(AccountException):
    pass

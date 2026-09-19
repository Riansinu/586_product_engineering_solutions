from abc import ABC, abstractmethod
from gdb.domain.i_account import IAccount
from gdb.exceptions import (
    InvalidAmountException,
    InsufficientBalanceException,
    InvalidPinException,
    AccountInactiveException,
    InvalidAccountDataException,
)


class BankAccount(IAccount, ABC):
    def __init__(self, account_number, name, age, balance, account_type, status="Active"):
        if age < 18:
            raise InvalidAccountDataException("Age must be at least 18")

        self._account_number = account_number
        self._name = name
        self._age = age
        self._balance = balance
        self._account_type = account_type
        self._status = status
        self._pin = None

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 18:
            raise InvalidAccountDataException("Age must be at least 18")
        self._age = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        self._pin = value

    @abstractmethod
    def get_minimum_balance(self) -> float:
        pass

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    def set_pin(self, new_pin) -> bool:
        if isinstance(new_pin, int) and 1000 <= new_pin <= 9999:
            self._pin = new_pin
            return True
        elif isinstance(new_pin, str) and len(new_pin) == 4 and new_pin.isdigit():
            self._pin = int(new_pin)
            return True
        raise InvalidPinException("PIN must be a 4-digit number")

    def verify_pin(self, entered_pin) -> bool:
        if self._pin is None:
            return False
        if isinstance(entered_pin, str) and entered_pin.isdigit():
            entered_pin = int(entered_pin)
        return self._pin == entered_pin

    def has_pin(self) -> bool:
        return self._pin is not None

    def close_account(self) -> bool:
        if self._status == "Inactive":
            return False
        self._status = "Inactive"
        return True

    def reopen_account(self) -> bool:
        if self._status == "Active":
            return False
        self._status = "Active"
        return True

    def deposit(self, amount: float) -> bool:
        if self._status != "Active":
            raise AccountInactiveException("Account is inactive")
        if amount <= 0:
            raise InvalidAmountException("Deposit amount must be positive")
        self._balance += amount
        return True

    def withdraw(self, amount: float, entered_pin=None) -> bool:
        if self._status != "Active":
            raise AccountInactiveException("Account is inactive")
        if self.has_pin():
            if entered_pin is None or not self.verify_pin(entered_pin):
                raise InvalidPinException("Invalid PIN entered")
        if amount <= 0:
            raise InvalidAmountException("Withdrawal amount must be positive")
        min_bal = self.get_minimum_balance()
        if self._balance - amount < min_bal:
            raise InsufficientBalanceException("Insufficient balance")
        self._balance -= amount
        return True

    def display_account_info(self) -> None:
        print("Account Number:", self._account_number)
        print("Name:", self._name)
        print("Age:", self._age)
        print("Balance:", self._balance)
        print("Account Type:", self._account_type)
        print("Status:", self._status)

from abc import ABC, abstractmethod


class IAccount(ABC):
    @property
    @abstractmethod
    def account_number(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def age(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

    @property
    @abstractmethod
    def account_type(self):
        pass

    @property
    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def deposit(self, amount: float) -> bool:
        pass

    @abstractmethod
    def withdraw(self, amount: float, entered_pin=None) -> bool:
        pass

    @abstractmethod
    def display_account_info(self) -> None:
        pass

    @abstractmethod
    def get_minimum_balance(self) -> float:
        pass

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

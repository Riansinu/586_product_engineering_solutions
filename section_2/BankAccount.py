from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, name, age, balance):
        if age < 18:
            age = 18

        if balance < 500.0:
            balance = 500.0

        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.status = "Active"
        self.pin = None
        self.transaction_log = []

    def deposit(self, amount):
        if self.status != "Active":
            return False

        if amount <= 0:
            return False

        self.balance += amount

        self.transaction_log.append(
            f"DEPOSIT: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    def withdraw(self, amount, entered_pin):
        if self.status != "Active":
            return False

        if self.pin is not None:
            if entered_pin is None or entered_pin != self.pin:
                return False

        if amount <= 0:
            return False

        if self.balance - amount < 500.0:
            return False

        self.balance -= amount

        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    def set_pin(self, new_pin):
        if 1000 <= new_pin <= 9999:
            self.pin = new_pin
            return True
        return False

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def has_pin(self):
        return self.pin is not None


class SavingsAccount(Account):
    pass


class CurrentAccount(Account):
    pass


class SalaryAccount(Account):
    pass


class InterestPolicy(ABC):
    @abstractmethod
    def calculate(self, balance):
        pass


class SavingsInterestPolicy(InterestPolicy):
    def calculate(self, balance):
        return balance * 0.04


class CurrentInterestPolicy(InterestPolicy):
    def calculate(self, balance):
        return balance * 0.01


class SalaryInterestPolicy(InterestPolicy):
    def calculate(self, balance):
        return balance * 0.05


class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass


class EmailNotificationService(NotificationService):
    def send(self, recipient, message):
        print(f"[EMAIL] To: {recipient} | {message}")


class SMSNotificationService(NotificationService):
    def send(self, recipient, message):
        print(f"[SMS] To: {recipient} | {message}")


class Bank:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def notify(self, recipient, message):
        self.notification_service.send(recipient, message)


class StatementGenerator:
    def generate(self, account):
        statement = [
            f"---- Statement for Account #{account.get_account_number()} ({account.get_name()}) ----"
        ]

        for entry in account.transaction_log:
            statement.append(entry)

        statement.append(f"Current Balance: Rs. {account.get_balance()}")
        statement.append("-----------------------------------------------------")

        return "\n".join(statement)
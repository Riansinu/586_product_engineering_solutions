class BankAccount:
    def __init__(self, account_number, name, age, balance, account_type):
        if age < 18:
            age = 18

        minimum_balance = 500.0 if account_type == "Savings" else 1000.0

        if balance < minimum_balance:
            balance = minimum_balance

        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type
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

        minimum_balance = 500.0 if self.account_type == "Savings" else 1000.0

        if self.balance - amount < minimum_balance:
            return False

        self.balance -= amount
        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )
        return True

    def close_account(self):
        if self.status == "Inactive":
            return False

        self.status = "Inactive"
        return True

    def reopen_account(self):
        if self.status == "Active":
            return False

        self.status = "Active"
        return True

    def set_pin(self, new_pin):
        if 1000 <= new_pin <= 9999:
            self.pin = new_pin
            return True
        return False

    def verify_pin(self, entered_pin):
        return self.pin is not None and self.pin == entered_pin

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

    def get_account_type(self):
        return self.account_type

    def has_pin(self):
        return self.pin is not None


class AccountRepository:
    def save(self, account):
        print(
            f"[DB] Saving account {account.get_account_number()} to MySQL..."
        )


class NotificationService:
    def send(self, recipient, message):
        print(f"[EMAIL] To: {recipient} | {message}")


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
from BankAccount import (
    SavingsAccount,
    CurrentAccount,
    SalaryAccount,
    SavingsInterestPolicy,
    CurrentInterestPolicy,
    SalaryInterestPolicy,
    EmailNotificationService,
    Bank,
    StatementGenerator
)


def main():
    savings = SavingsAccount(
        101,
        "Ravi",
        17,
        200
    )

    current = CurrentAccount(
        102,
        "Ravi",
        20,
        2000
    )

    salary = SalaryAccount(
        103,
        "Ravi",
        25,
        5000
    )

    savings.set_pin(1234)

    savings.deposit(1000)
    savings.withdraw(500, 1234)

    current.deposit(2000)
    current.withdraw(500, None)

    salary.deposit(3000)
    salary.withdraw(1000, None)

    savings_policy = SavingsInterestPolicy()
    current_policy = CurrentInterestPolicy()
    salary_policy = SalaryInterestPolicy()

    print(
        "Savings Interest: Rs. "
        + str(savings_policy.calculate(savings.get_balance()))
    )

    print(
        "Current Interest: Rs. "
        + str(current_policy.calculate(current.get_balance()))
    )

    print(
        "Salary Interest: Rs. "
        + str(salary_policy.calculate(salary.get_balance()))
    )

    bank = Bank(EmailNotificationService())

    bank.notify(
        savings.get_name(),
        "Account operations completed successfully."
    )

    statement_generator = StatementGenerator()

    print()
    print(statement_generator.generate(savings))


if __name__ == "__main__":
    main()
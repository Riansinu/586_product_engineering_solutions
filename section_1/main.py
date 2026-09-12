from BankAccount import (
    BankAccount,
    AccountRepository,
    NotificationService,
    StatementGenerator
)


def main():
    account = BankAccount(
        101,
        "Ravi",
        17,
        200,
        "Savings"
    )

    account.set_pin(1234)

    account.deposit(1000)

    account.withdraw(500, 1234)

    account.withdraw(500, 9999)

    repository = AccountRepository()
    notification_service = NotificationService()
    statement_generator = StatementGenerator()

    repository.save(account)

    notification_service.send(
        account.get_name(),
        "Account operations completed successfully."
    )

    print(statement_generator.generate(account))

    print(
        "Interest earned: Rs. 0.0"
    )


if __name__ == "__main__":
    main()
    
from gdb.domain import BankAccount, SavingsAccount, CurrentAccount


def test_abstract_hierarchy():
    try:
        BankAccount("B1", "Test", 20, 1000.0, "Generic")
        assert False, "Should not instantiate abstract BankAccount"
    except TypeError:
        pass

    sav = SavingsAccount("S1", "Alice", 25, 2000.0)
    cur = CurrentAccount("C1", "Bob", 30, 1000.0)

    assert sav.get_minimum_balance() == 500.0
    assert cur.get_minimum_balance() == -10000.0

    assert sav.calculate_interest() == 80.0
    assert cur.calculate_interest() == 0.0

    accounts: list[BankAccount] = [sav, cur]
    for acc in accounts:
        assert isinstance(acc, BankAccount)
        acc.deposit(100.0)


if __name__ == "__main__":
    test_abstract_hierarchy()

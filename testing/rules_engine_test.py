from gdb.rules import AccountRulesEngine, AccountRulesPropertiesLoader
from gdb.factory import AccountFactory
from gdb.exceptions import InsufficientBalanceException


def test_rules_engine():
    engine = AccountRulesEngine("config")

    assert engine.get_minimum_balance("SAVINGS") == 1000.0
    assert engine.get_interest_rate("SAVINGS") == 4.0

    assert engine.get_minimum_balance("CURRENT") == 0.0
    assert engine.get_overdraft_limit("CURRENT") == 10000.0

    assert engine.get_interest_rate("FIXEDDEPOSIT") == 6.5

    assert engine.get_minimum_balance("SALARY") == 0.0
    assert engine.get_interest_rate("SALARY") == 4.0

    sav = AccountFactory.create_account("SAVINGS", "S1", "Alice", 25, 2000.0)
    assert engine.validate_withdrawal(sav, 500.0) is True

    try:
        engine.validate_withdrawal(sav, 1500.0)
        assert False, "Should have raised InsufficientBalanceException"
    except InsufficientBalanceException:
        pass

    engine.reload_rules("config")
    assert engine.get_interest_rate("FIXEDDEPOSIT") == 6.5


if __name__ == "__main__":
    test_rules_engine()

from gdb.domain.i_account import IAccount
from gdb.exceptions import (
    AccountInactiveException,
    InvalidAmountException,
    InsufficientBalanceException,
    InvalidAccountDataException,
)
from gdb.rules.account_rules_properties_loader import AccountRulesPropertiesLoader


class AccountRulesEngine:
    def __init__(self, config_dir: str = "config"):
        self._config_dir = config_dir
        self._default_rules = {
            "SAVINGS": {
                "minimum_balance": 1000.0,
                "interest_rate": 4.0,
                "overdraft_limit": 0.0,
            },
            "CURRENT": {
                "minimum_balance": 0.0,
                "interest_rate": 0.0,
                "overdraft_limit": 10000.0,
            },
            "SALARY": {
                "minimum_balance": 0.0,
                "interest_rate": 4.0,
                "overdraft_limit": 0.0,
            },
            "FIXEDDEPOSIT": {
                "minimum_balance": 1000.0,
                "interest_rate": 6.5,
                "overdraft_limit": 0.0,
            },
        }
        self._rules = dict(self._default_rules)
        self.reload_rules(config_dir)

    def reload_rules(self, config_dir: str = None):
        if config_dir is not None:
            self._config_dir = config_dir
        loaded = AccountRulesPropertiesLoader.load_all_rules(self._config_dir)
        if loaded:
            for acc_type, props in loaded.items():
                if acc_type not in self._rules:
                    self._rules[acc_type] = {}
                self._rules[acc_type].update(props)

    def _normalize_type(self, account_type: str) -> str:
        return account_type.upper().replace("_", "").replace(" ", "")

    def get_minimum_balance(self, account_type: str) -> float:
        acc_type = self._normalize_type(account_type)
        if acc_type not in self._rules:
            raise InvalidAccountDataException(f"Unknown account type: {account_type}")
        return float(self._rules[acc_type].get("minimum_balance", 0.0))

    def get_interest_rate(self, account_type: str) -> float:
        acc_type = self._normalize_type(account_type)
        if acc_type not in self._rules:
            raise InvalidAccountDataException(f"Unknown account type: {account_type}")
        return float(self._rules[acc_type].get("interest_rate", 0.0))

    def get_overdraft_limit(self, account_type: str) -> float:
        acc_type = self._normalize_type(account_type)
        if acc_type not in self._rules:
            raise InvalidAccountDataException(f"Unknown account type: {account_type}")
        return float(self._rules[acc_type].get("overdraft_limit", 0.0))

    def validate_withdrawal(self, account: IAccount, amount: float) -> bool:
        if account.status != "Active":
            raise AccountInactiveException("Account is inactive")
        if amount <= 0:
            raise InvalidAmountException("Withdrawal amount must be positive")

        acc_type = self._normalize_type(account.account_type)
        min_bal = self.get_minimum_balance(acc_type)
        overdraft = self.get_overdraft_limit(acc_type)

        if acc_type == "CURRENT":
            limit = -overdraft
        else:
            limit = min_bal

        if account.balance - amount < limit:
            raise InsufficientBalanceException("Insufficient balance for withdrawal")

        return True

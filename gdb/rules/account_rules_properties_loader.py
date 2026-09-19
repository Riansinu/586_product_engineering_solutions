import os


class AccountRulesPropertiesLoader:
    @staticmethod
    def load_properties(file_path: str) -> dict:
        props = {}
        if not os.path.exists(file_path):
            return props
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or line.startswith("!"):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip()
                    try:
                        if "." in val:
                            val = float(val)
                        else:
                            val = float(int(val))
                    except ValueError:
                        pass
                    props[key] = val
        return props

    @staticmethod
    def load_all_rules(config_dir: str = "config") -> dict:
        rules = {}
        mapping = {
            "SAVINGS": "savings.properties",
            "CURRENT": "current.properties",
            "FIXEDDEPOSIT": "fixeddeposit.properties",
            "SALARY": "salary.properties",
        }
        for acc_type, filename in mapping.items():
            path = os.path.join(config_dir, filename)
            props = AccountRulesPropertiesLoader.load_properties(path)
            if props:
                rules[acc_type] = props
        return rules

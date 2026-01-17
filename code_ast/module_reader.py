import os

# Absolute path to ERPNext source code
ERP_BASE_PATH = r"E:\PeralThoughts\ERP\erpnext\erpnext"


def find_module_file(module_name: str) -> str:
    for root, _, files in os.walk(ERP_BASE_PATH):
        for file in files:
            if module_name == file:
                return os.path.join(root, file)

    raise FileNotFoundError(
        f"{module_name} not found under {ERP_BASE_PATH}"
    )

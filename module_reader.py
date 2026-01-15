import os

IGNORE_DIRS = {"__pycache__", "tests", ".git", "node_modules"}

def get_python_files(root_path):
    py_files = []
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

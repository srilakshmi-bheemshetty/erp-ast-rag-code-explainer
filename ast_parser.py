import ast

def extract_functions(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        tree = ast.parse(f.read())

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                "function": node.name,
                "inputs": [arg.arg for arg in node.args.args],
                "behavior": summarize_behavior(node)
            })

    return functions


def summarize_behavior(func_node):
    calls = set()
    returns = False

    for node in ast.walk(func_node):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                calls.add(node.func.attr)
            elif isinstance(node.func, ast.Name):
                calls.add(node.func.id)
        if isinstance(node, ast.Return):
            returns = True

    behavior = []
    if calls:
        behavior.append(f"Uses calls: {', '.join(sorted(calls))}")
    if returns:
        behavior.append("Returns a value")

    return "; ".join(behavior) if behavior else "Defines business logic"

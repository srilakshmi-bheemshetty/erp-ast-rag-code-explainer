import os

def build_documents(file_path, ast_data, erp_root):
    docs = []
    module = os.path.relpath(file_path, erp_root).split(os.sep)[0]

    for fn in ast_data:
        doc = f"""
Module: {module}
File: {file_path}
Function: {fn['function']}
Inputs: {fn['inputs']}
Behavior: {fn['behavior']}
"""
        docs.append(doc.strip())

    return docs

from rag.pipeline import rag_pipeline
from code_ast.ast_parser import analyze_file
from code_ast.module_reader import find_module_file

print("---- RAG OUTPUT ----")
print(rag_pipeline("How does ERPNext manage stock?"))

print("\n---- AST OUTPUT ----")
file_path = find_module_file("stock_ledger.py")
print(analyze_file(file_path))

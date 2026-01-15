from module_reader import get_python_files
from ast_parser import extract_functions
from knowledge_builder import build_documents
from vector_store import build_vector_store
from retriever import retrieve_context
from rag_explainer import explain
from config import ERP_SOURCE_PATH

def index_erp():
    all_docs = []
    files = get_python_files(ERP_SOURCE_PATH)

    print(f"Indexing {len(files)} Python files...")

    for file in files:
        try:
            ast_data = extract_functions(file)
            docs = build_documents(file, ast_data, ERP_SOURCE_PATH)
            all_docs.extend(docs)
        except Exception:
            continue

    build_vector_store(all_docs)
    print("✅ ERP indexing completed")

def chat():
    while True:
        query = input("\nAsk about ERP code (or 'exit'): ")
        if query.lower() == "exit":
            break

        context = retrieve_context(query)
        answer = explain(query, context)
        print("\nAnswer:\n", answer)

if __name__ == "__main__":
    print("1. Build ERP Index")
    print("2. Ask Questions")

    choice = input("Choose (1/2): ")

    if choice == "1":
        index_erp()
    else:
        chat()

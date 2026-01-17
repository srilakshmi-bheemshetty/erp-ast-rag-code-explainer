# hybrid/pipeline.py

from rag.pipeline import rag_pipeline
from code_ast.ast_parser import analyze_file
from code_ast.module_reader import find_module_file


def hybrid_pipeline(module_name: str, question: str) -> str:
    """X
    Hybrid pipeline:
    - AST for source-of-truth structure
    - RAG for semantic explanation
    """

    # ---------- AST ----------
    try:
        file_path = find_module_file(module_name)
        ast_result = analyze_file(file_path)
    except Exception as e:
        ast_result = f"AST analysis failed: {e}"

    # ---------- RAG ----------
    try:
        rag_result = rag_pipeline(question)
    except Exception as e:
        rag_result = f"RAG failed: {e}"

    # ---------- Merge ----------
    response = f"""
=== AST ANALYSIS (Source of Truth) ===
{ast_result}

=== RAG EXPLANATION (Semantic Context) ===
{rag_result}
"""
    return response.strip()

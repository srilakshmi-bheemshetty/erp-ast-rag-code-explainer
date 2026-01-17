import sys
import os
import logging

from mcp.server.fastmcp import FastMCP

# ---- basic logging (NO emojis, Windows-safe) ----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ---- ensure project root is in path ----
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ---- imports from your project ----
from code_ast.ast_parser import analyze_file
from code_ast.module_reader import find_module_file

from rag.pipeline import rag_pipeline
from hybrid.pipeline import hybrid_pipeline  # make sure this exists

# ---- create MCP server ----
mcp = FastMCP("erp-ai-assistant")

logging.info("Starting ERP AI Assistant MCP server")

# =================================================
# AST ONLY TOOL
# =================================================
@mcp.tool()
def analyze_erp_module(module_name: str):
    """
    AST-only analysis of an ERPNext Python module.
    Returns function names, arguments, and structure.
    """
    try:
        file_path = find_module_file(module_name)
        result = analyze_file(file_path)
        return {
            "module": module_name,
            "analysis": result
        }
    except Exception as e:
        logging.exception("AST analysis failed")
        return {"error": str(e)}

# =================================================
# RAG ONLY TOOL
# =================================================
@mcp.tool()
def rag_explain(question: str):
    """
    RAG-based explanation using indexed ERPNext documentation/code.
    """
    try:
        answer = rag_pipeline(question)
        return {
            "question": question,
            "answer": answer
        }
    except Exception as e:
        logging.exception("RAG explanation failed")
        return {"error": str(e)}

# =================================================
# HYBRID (AST + RAG) TOOL
# =================================================
@mcp.tool()
def hybrid_explain(module_name: str, question: str):
    """
    Hybrid explanation combining AST (source of truth)
    with RAG (contextual understanding).
    """
    try:
        result = hybrid_pipeline(module_name, question)
        return result
    except Exception as e:
        logging.exception("Hybrid explanation failed")
        return {"error": str(e)}

# =================================================
# ENTRYPOINT (REQUIRED)
# =================================================
if __name__ == "__main__":
    logging.info("MCP server initialized, waiting for client")
    mcp.run()

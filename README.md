# ERP AI Assistant – AST, RAG & Hybrid MCP Architecture

An AI-powered **ERPNext Code Explainer** that combines **AST-based source analysis**, **RAG-based semantic retrieval**, and a **Hybrid pipeline**, exposed via **MCP (Model Context Protocol)** for tool-based AI interaction.

This project helps developers and interns understand **complex ERPNext modules** (like stock, ledger, accounting) accurately and safely.

---

## 🚀 Key Features

### 🔹 AST (Abstract Syntax Tree) – Source of Truth
- Parses real ERPNext Python files
- Extracts:
  - Functions
  - Arguments
  - Line numbers
- Guarantees **no hallucination**
- Used for **accurate technical explanations**

### 🔹 RAG (Retrieval-Augmented Generation)
- Builds a vector index from ERPNext code
- Retrieves semantically relevant code snippets
- Helps explain **intent and flow**
- Uses embeddings + LLM explanation

### 🔹 Hybrid Pipeline (AST + RAG)
- AST → factual structure
- RAG → semantic understanding
- Produces **clear, developer-friendly explanations**

### 🔹 MCP Server Integration
- Exposes pipelines as MCP tools
- Can be used inside **Cursor / Claude / MCP-compatible agents**
- Tools available:
  - `analyze_erp_module` (AST only)
  - `rag_explain` (RAG only)
  - `hybrid_explain` (AST + RAG)

---

## 📁 Project Structure


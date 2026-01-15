# ERP AST-Based RAG Code Explainer

A generic **Retrieval-Augmented Generation (RAG)** system that helps developers understand large ERP codebases (such as ERPNext) by **statically analyzing Python source code using Abstract Syntax Trees (AST)** and generating **accurate, context-grounded explanations** using an LLM (Groq).

This project is designed to assist **developers, interns, and new team members** in quickly understanding complex ERP modules without executing ERP code.

---

## 🚀 Key Features

- 🔍 **AST-based static code analysis** (no runtime execution)
- 🧠 **RAG architecture** for accurate and grounded answers
- ⚡ **Groq LLM integration** for ultra-fast explanations
- 📦 **Local embeddings + FAISS** (no API quota limits)
- 🧩 Works with **any ERP module** (not limited to one module)
- 🚫 Refuses out-of-context questions (hallucination control)
- 🔐 Safe, deterministic, and scalable

---

## 🧠 Why AST + RAG?

### Why AST?
- No code execution
- Safe and deterministic
- Accurate extraction of:
  - Function names
  - Inputs and parameters
  - Internal function calls
  - Structural behavior

### Why RAG?
- Ensures answers are generated **only from retrieved code context**
- Prevents hallucinations
- Scales efficiently to **large ERP codebases**

---

## 🏗️ Architecture Overview



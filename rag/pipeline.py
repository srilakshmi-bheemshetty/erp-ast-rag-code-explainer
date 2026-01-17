from rag.retriever import get_retriever
from rag.rag_explainer import explain

MAX_CHUNKS = 4          # limit number of docs
MAX_CHARS = 3000        # hard limit on context size


def rag_pipeline(question: str) -> str:
    retriever = get_retriever()
    docs = retriever.get_relevant_documents(question)

    if not docs:
        return "No relevant documents found."

    # Limit number of chunks
    docs = docs[:MAX_CHUNKS]

    context_parts = []
    current_length = 0

    for d in docs:
        text = d.page_content if hasattr(d, "page_content") else str(d)

        if current_length + len(text) > MAX_CHARS:
            remaining = MAX_CHARS - current_length
            context_parts.append(text[:remaining])
            break

        context_parts.append(text)
        current_length += len(text)

    context = "\n\n".join(context_parts)

    return explain(question, context)

from rag.vector_store import load_vector_store


class Document:
    def __init__(self, page_content: str):
        self.page_content = page_content


def get_retriever():
    _, documents = load_vector_store()

    class Retriever:
        def get_relevant_documents(self, query: str):
            # TEMP: return first few text chunks
            return [Document(text) for text in documents[:5]]

    return Retriever()

import pickle
import faiss


def load_vector_store():
    with open("erp_code_index/index.pkl", "rb") as f:
        docstore = pickle.load(f)

    index = faiss.read_index("erp_code_index/index.faiss")

    # Extract actual text documents
    documents = []

    if hasattr(docstore, "_dict"):  # InMemoryDocstore
        for doc in docstore._dict.values():
            documents.append(doc.page_content)

    return index, documents

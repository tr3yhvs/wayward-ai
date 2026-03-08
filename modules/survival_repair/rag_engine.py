"""RAG engine with vector search for offline knowledge base."""
import os
import pickle
import numpy as np

KNOWLEDGE_BASE_PATH = os.path.join(os.path.dirname(__file__), "knowledge_base")
VECTOR_STORE_PATH = os.path.join(os.path.dirname(__file__), "vector_store")

def search_knowledge(query, top_k=3):
    index_path = os.path.join(VECTOR_STORE_PATH, "index.faiss")
    docs_path = os.path.join(VECTOR_STORE_PATH, "docs.pkl")

    if not os.path.exists(index_path):
        from modules.survival_repair.vector_store.vectorizer import build_index
        build_index()

    import faiss
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("all-MiniLM-L6-v2")
    index = faiss.read_index(index_path)
    with open(docs_path, "rb") as f:
        docs = pickle.load(f)

    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, top_k)

    results = []
    for i in indices[0]:
        if i < len(docs):
            results.append(docs[i])
    return results

def answer_from_knowledge(query):
    results = search_knowledge(query, top_k=2)
    if not results:
        return "No relevant information found in knowledge base."
    response = ""
    for r in results:
        response += r["text"] + "\n\n"
    return response.strip()

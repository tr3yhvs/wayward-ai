"""Vector store builder for knowledge base."""
import os
import glob
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

KNOWLEDGE_BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "knowledge_base")
VECTOR_STORE_PATH = os.path.dirname(__file__)
MODEL_NAME = "all-MiniLM-L6-v2"

def build_index():
    model = SentenceTransformer(MODEL_NAME)
    docs = []
    texts = []

    for filepath in glob.glob(os.path.join(KNOWLEDGE_BASE_PATH, "*.md")):
        with open(filepath, encoding="utf-8-sig") as f:
            content = f.read()
        chunks = [c.strip() for c in content.split("\n\n") if len(c.strip()) > 30]
        for chunk in chunks:
            docs.append({"file": os.path.basename(filepath), "text": chunk})
            texts.append(chunk)

    print(f"Found {len(texts)} chunks from {len(docs)} sections")

    if not texts:
        print("No texts found!")
        return None, []

    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, os.path.join(VECTOR_STORE_PATH, "index.faiss"))
    with open(os.path.join(VECTOR_STORE_PATH, "docs.pkl"), "wb") as f:
        pickle.dump(docs, f)

    print(f"Built index with {len(texts)} chunks")
    return index, docs

if __name__ == "__main__":
    build_index()

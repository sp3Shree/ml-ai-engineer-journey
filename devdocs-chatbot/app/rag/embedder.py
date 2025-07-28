import os
import json
import pickle
import faiss
from pathlib import Path
from sentence_transformers import SentenceTransformer

CHUNK_PATH = "data/chunks/chunks.jsonl"
VECTOR_STORE_DIR = "data/vector_store/"
INDEX_FILE = os.path.join(VECTOR_STORE_DIR, "faiss.index")
METADATA_FILE = os.path.join(VECTOR_STORE_DIR, "metadata.pkl")

def load_chunks(jsonl_path):
    chunks = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line.strip()))
    return chunks

def save_metadata(metadata):
    with open(METADATA_FILE, "wb") as f:
        pickle.dump(metadata, f)

def main():
    os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

    print("🔄 Loading chunks...")
    chunks = load_chunks(CHUNK_PATH)
    texts = [chunk["text"] for chunk in chunks]
    metadata = [ {k: v for k, v in chunk.items() if k != "text"} for chunk in chunks ]

    print("🧠 Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, show_progress_bar=True)

    print("📦 Building FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print("💾 Saving FAISS index and metadata...")
    faiss.write_index(index, INDEX_FILE)
    save_metadata(metadata)

    print(f"✅ Indexed {len(embeddings)} chunks")

if __name__ == "__main__":
    main()

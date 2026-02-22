from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import os

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Persistent Chroma client
client = chromadb.Client(
    Settings(
        persist_directory="db",
        is_persistent=True
    )
)

# Delete collection if exists (clean reset)
try:
    client.delete_collection("company_docs")
    print("🗑 Old collection deleted")
except:
    pass

# Create fresh collection
collection = client.create_collection("company_docs")

# Check document exists
if not os.path.exists("document.txt"):
    print("❌ document.txt not found in project folder")
    exit()

# Read document
with open("document.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chunks
chunks = [chunk.strip() for chunk in text.split("\n") if chunk.strip()]

# Store embeddings
for i, chunk in enumerate(chunks):
    embedding = embed_model.encode(chunk).tolist()

    collection.add(
        documents=[chunk],
        embeddings=[embedding],
        ids=[str(i)]
    )

print("✅ Documents stored successfully in ChromaDB!")

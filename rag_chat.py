import ollama
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to persistent Chroma DB
client = chromadb.Client(
    Settings(
        persist_directory="db",
        is_persistent=True
    )
)

collection = client.get_collection("company_docs")

print("🤖 RAG Chatbot Ready! Type 'exit' to quit.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("👋 Exiting chatbot...")
        break

    # Convert question to embedding
    query_embedding = embed_model.encode(question).tolist()

    # Retrieve similar documents
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    if not results["documents"][0]:
        print("⚠️ No relevant information found.")
        continue

    context = "\n".join(results["documents"][0])

    # Create contextual prompt
    prompt = f"""
You are an AI assistant.

Use the context below if relevant.
If the context does not contain the answer,
you may answer using your general knowledge.

Context:
{context}

Question:
{question}
"""

    # Call Ollama
    response = ollama.chat(
        model="phi3:mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nAI:\n")
    print(response["message"]["content"])

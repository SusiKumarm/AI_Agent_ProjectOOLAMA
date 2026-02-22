import streamlit as st
import ollama
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to DB
client = chromadb.Client(
    Settings(
        persist_directory="db",
        is_persistent=True
    )
)

collection = client.get_collection("company_docs")

st.set_page_config(page_title="Local RAG Chatbot")
st.title("🤖 Local AI RAG Assistant")
st.write("Private. Offline. Powered by Ollama.")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask a question")

if user_input:
    st.session_state.messages.append(("user", user_input))

    query_embedding = embed_model.encode(user_input).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
    You are an AI assistant.

Use the context below if relevant.
If the context does not contain the answer,
you may answer using your general knowledge.

    Context:
    {context}

    Question:
    {user_input}
    """

    response = ollama.chat(
        model="phi3:mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    st.session_state.messages.append(("assistant", answer))

for role, msg in st.session_state.messages:
    if role == "user":
        st.write(f"🧑 You: {msg}")
    else:
        st.write(f"🤖 AI: {msg}")

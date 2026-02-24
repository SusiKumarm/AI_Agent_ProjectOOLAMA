import streamlit as st
import ollama
import os
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# ==============================
# CONFIG
# ==============================

GEMINI_MODEL = "gemini-1.5-flash"
OLLAMA_MODEL = "phi3:mini"

# Configure Gemini
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# ==============================
# LOAD EMBEDDING MODEL
# ==============================

@st.cache_resource
def load_embed_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

embed_model = load_embed_model()

# ==============================
# CONNECT CHROMA
# ==============================

@st.cache_resource
def get_collection():
    client = chromadb.Client(
        Settings(
            persist_directory="db",
            is_persistent=True
        )
    )
    return client.get_collection("company_docs")

collection = get_collection()

# ==============================
# STREAMLIT UI
# ==============================

st.set_page_config(page_title="RAG AI Assistant")
st.title("🤖 RAG AI Assistant")
st.write("Switch between Cloud Gemini and Local Ollama.")

# 🔽 MODEL DROPDOWN
selected_model = st.selectbox(
    "Choose Model",
    ["Gemini (Cloud)", "Ollama (Local)"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask a question")

# ==============================
# MAIN LOGIC
# ==============================

if user_input:

    st.session_state.messages.append(("user", user_input))

    # 1️⃣ Embed Question
    query_embedding = embed_model.encode(user_input).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = ""
    if results["documents"] and results["documents"][0]:
        context = "\n".join(results["documents"][0])

    prompt = f"""
You are an AI assistant.

Use the context below if relevant.
If context does not contain answer, use general knowledge.

Context:
{context}

Question:
{user_input}
"""

    answer = ""

    # ==============================
    # GEMINI FIRST (if selected)
    # ==============================

    if selected_model == "Gemini (Cloud)":
        try:
            model = genai.GenerativeModel(GEMINI_MODEL)
            response = model.generate_content(prompt)
            answer = response.text

        except Exception as e:
            st.warning("⚠️ Gemini failed. Falling back to Ollama...")
            answer = ollama.chat(
                model=OLLAMA_MODEL,
                messages=[{"role": "user", "content": prompt}]
            )["message"]["content"]

    # ==============================
    # OLLAMA DIRECT
    # ==============================

    else:
        answer = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )["message"]["content"]

    st.session_state.messages.append(("assistant", answer))

# ==============================
# DISPLAY CHAT
# ==============================

for role, msg in st.session_state.messages:
    if role == "user":
        st.write(f"🧑 You: {msg}")
    else:
        st.write(f"🤖 AI: {msg}")
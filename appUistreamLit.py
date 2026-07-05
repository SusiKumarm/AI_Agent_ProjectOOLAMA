import streamlit as st
import ollama
import os
import google.generativeai as genai
from sentence_transformers import SentenceTransformer   # Converts text → vectors
import chromadb                                         # Vector database for company docs
from chromadb.config import Settings
import json
from tools.weather import get_weather                   # Custom weather tool

# ==============================================================
# SECTION 1: CONFIG
# ==============================================================

GEMINI_MODEL = "gemini-2.5-flash"   # Cloud model (needs GOOGLE_API_KEY)
OLLAMA_MODEL = "phi3:mini"          # Local model (runs via Ollama)

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# ==============================================================
# SECTION 2: LOAD EMBEDDING MODEL
# Converts text → vectors for ChromaDB similarity search
# @st.cache_resource = loads once, reused across reruns
# ==============================================================

@st.cache_resource
def load_embed_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

embed_model = load_embed_model()

# ==============================================================
# SECTION 3: CONNECT TO CHROMADB
# Stores your company documents as vectors.
# get_or_create_collection = creates on first run, reuses after.
# ==============================================================

@st.cache_resource
def get_collection():
    client = chromadb.Client(
        Settings(
            persist_directory="db",
            is_persistent=True
        )
    )
    return client.get_or_create_collection("company_docs")

collection = get_collection()

# ==============================================================
# SECTION 4: STREAMLIT UI SETUP
# ==============================================================

st.set_page_config(page_title="RAG AI Assistant")
st.title("🤖 RAG AI Assistant")
st.write("Switch between Cloud Gemini and Local Ollama.")

selected_model = st.selectbox(
    "Choose Model",
    ["Gemini (Cloud)", "Ollama (Local)"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask a question")

# ==============================================================
# SECTION 5: MAIN LOGIC
# Flow:
#   Step A → Tool selector (is this a weather question?)
#   Step B → If weather: call weather API, done.
#   Step C → If not weather:
#               Search ChromaDB for relevant company docs
#               If docs found    → answer using docs (RAG mode)
#               If no docs found → answer from model's own knowledge (general mode)
#               Either way, Ollama or Gemini always gives a response.
# ==============================================================

if user_input:

    st.session_state.messages.append(("user", user_input))

    # ----------------------------------------------------------
    # STEP A: TOOL SELECTION
    # Ask Phi3 to decide: is this a weather query or not?
    # We use a tiny local model here to avoid wasting API calls on routing.
    # ----------------------------------------------------------

    tool_prompt = f"""
You are a tool selector.

Available tools:
1. weather

If the user is asking about weather, temperature, or wind, return ONLY this exact JSON:
{{"tool":"weather"}}

For ALL other questions return ONLY this exact JSON:
{{"tool":"none"}}

User Question:
{user_input}
"""

    tool_response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": tool_prompt}]
    )["message"]["content"]

    st.write("Tool Response:", tool_response)

    # Parse JSON response from Phi3
    try:
        tool_request = json.loads(tool_response)
    except Exception:
        # Phi3 sometimes wraps JSON in extra explanation text.
        # Fallback: do a simple string search for the intent.
        tool_request = {"tool": "none"}
        if '"tool":"weather"' in tool_response.replace(" ", ""):
            tool_request = {"tool": "weather"}

    # ----------------------------------------------------------
    # STEP B: WEATHER BRANCH
    # Tool selector said "weather" → call weather API directly.
    # No LLM or ChromaDB needed here.
    # ----------------------------------------------------------

    if tool_request.get("tool") == "weather":

        weather_data = get_weather()
        answer = f"""
Current Temperature: {weather_data['temperature']}°C
Wind Speed: {weather_data['windspeed']} km/h
"""
        st.session_state.messages.append(("assistant", answer))
        st.rerun()

    # ----------------------------------------------------------
    # STEP C: GENERAL / RAG BRANCH
    # Tool selector said "none" → handle with LLM.
    # First, try to find relevant company docs in ChromaDB.
    # Then build the prompt based on what we found.
    # ----------------------------------------------------------

    else:

        # STEP C1: Search ChromaDB for relevant company document chunks
        query_embedding = embed_model.encode(user_input).tolist()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        # Check if ChromaDB returned any useful documents
        context = ""
        if results["documents"] and results["documents"][0]:
            context = "\n".join(results["documents"][0])

        # STEP C2: Build prompt based on whether context was found or not
        if context.strip():
            # RAG MODE: Company docs found → answer from documents
            # Tell the model to prioritise the context but allow general knowledge too
            st.info("📄 Answering from company documents...")
            prompt = f"""
You are a helpful AI assistant.

Use the context below to answer the question.
If the context is not sufficient, you may also use your general knowledge.

Context:
{context}

Question:
{user_input}

Answer:
"""
        else:
            # GENERAL MODE: No company docs found → answer from model's own knowledge
            # FIX: Previously the app sent an empty context and gave a weak answer.
            # Now we explicitly tell the model to use its own knowledge freely.
            st.info("💡 No company docs found. Answering from general knowledge...")
            prompt = f"""
You are a helpful AI assistant with broad general knowledge.

Answer the following question clearly and in detail using your own knowledge.

Question:
{user_input}

Answer:
"""

        # STEP C3: Send prompt to selected model
        answer = ""

        if selected_model == "Gemini (Cloud)":
            try:
                model = genai.GenerativeModel(GEMINI_MODEL)
                response = model.generate_content(prompt)
                answer = response.text

            except Exception as e:
                # Gemini failed (quota/network/key issue) → fall back to Ollama
                st.warning(f"⚠️ Gemini failed ({e}). Falling back to Ollama...")
                answer = ollama.chat(
                    model=OLLAMA_MODEL,
                    messages=[{"role": "user", "content": prompt}]
                )["message"]["content"]

        else:
            # Ollama (local) selected — works for both RAG and general questions
            # phi3:mini can answer general knowledge questions fine when asked clearly
            answer = ollama.chat(
                model=OLLAMA_MODEL,
                messages=[{"role": "user", "content": prompt}]
            )["message"]["content"]

        st.session_state.messages.append(("assistant", answer))
        st.rerun()

# ==============================================================
# SECTION 6: DISPLAY CHAT HISTORY
# Renders on every Streamlit load/rerun.
# ==============================================================

for role, msg in st.session_state.messages:
    if role == "user":
        st.write(f"🧑 You: {msg}")
    else:
        st.write(f"🤖 AI: {msg}")
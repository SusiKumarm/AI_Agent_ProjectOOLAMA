# High-Level AI Concepts Learned

## What is an LLM?

An LLM (Large Language Model) is an AI model trained on massive amounts of text data that can understand and generate human-like language.

Examples:

* Phi-3
* Gemma
* Mistral
* Gemini
* GPT

---

## What is Ollama?

Ollama is a local AI runtime that allows developers to download, run, and interact with LLMs on their own machine without using cloud APIs.

Key Benefit:

* Offline execution
* Privacy
* No API cost

---

## What is Prompt Engineering?

Prompt engineering is the process of designing instructions and context sent to an LLM to improve the quality and accuracy of responses.

Example:

Poor Prompt:
"Testing"

Better Prompt:
"Generate positive, negative, and boundary test cases for a login page."

---

## What are Embeddings?

Embeddings are numerical vector representations of text that capture semantic meaning.

Example:

Texts:

* Car
* Automobile

have different words but similar meanings.

Embeddings place them close together in vector space.

Purpose:

* Semantic Search
* Recommendations
* RAG Systems

---

## What is a Vector?

A vector is a list of numbers representing the meaning of data.

Example:

```text
[0.23, -0.11, 0.76, 0.45]
```

LLMs do not understand text directly; they process vector representations.

---

## What is an Embedding Model?

An embedding model converts text into vectors.

Example:

Sentence:
"Insurance Policy"

↓

Embedding Model

↓

Vector:
[0.45, -0.23, 0.89, ...]

Example Model:

* all-MiniLM-L6-v2

---

## What is a Vector Database?

A vector database stores embeddings and allows similarity searches.

Examples:

* ChromaDB
* Pinecone
* Weaviate
* Milvus

Purpose:

* Find semantically similar content

---

## What is Semantic Search?

Semantic search finds information based on meaning rather than exact keywords.

Traditional Search:

Search:
"car"

Matches:
"car"

Semantic Search:

Search:
"automobile"

Can still find:
"car"

because meanings are similar.

---

## What is ChromaDB?

ChromaDB is an open-source vector database used to store embeddings and perform similarity searches.

In this project:

Documents
↓
Embeddings
↓
ChromaDB
↓
Similarity Search

---

## What is RAG?

RAG stands for Retrieval-Augmented Generation.

It combines:

1. Information Retrieval
2. LLM Response Generation

Flow:

Question
↓
Retrieve Relevant Documents
↓
Send Context to LLM
↓
Generate Answer

Purpose:
Allow LLMs to answer questions using external knowledge.

---

## Why Do We Need RAG?

LLMs have limited knowledge and can hallucinate.

RAG helps by:

* Using latest documents
* Using company-specific information
* Improving accuracy
* Reducing hallucinations

---

## What is Context Injection?

Context injection means adding relevant information to a prompt before sending it to the model.

Example:

Question:
"What is the policy premium?"

Retrieved Document:
"The premium amount is ₹5000."

Prompt Sent to LLM:

Context:
"The premium amount is ₹5000."

Question:
"What is the policy premium?"

The model now answers using supplied information.

---

## What is Chunking?

Chunking is the process of splitting large documents into smaller pieces before generating embeddings.

Why?

LLMs and vector databases work better with smaller sections of text.

Example:

100-page PDF

↓

Multiple Chunks

↓

Embeddings

↓

Storage

---

## What is Similarity Search?

Similarity search finds the most relevant vectors to a user query.

Process:

Question
↓
Convert to Embedding
↓
Compare with Stored Embeddings
↓
Return Closest Matches

---

## What is Streamlit?

Streamlit is a Python framework used to build web applications quickly.

Benefits:

* Fast development
* Minimal frontend coding
* Good for AI applications

---

## What is Local AI?

Local AI means running models entirely on your own machine without sending data to cloud providers.

Benefits:

* Privacy
* Security
* No API cost
* Offline operation

---

## What is Cloud AI?

Cloud AI runs models hosted by providers.

Examples:

* Gemini
* OpenAI
* Anthropic

Benefits:

* Powerful models
* Easy scalability

Drawbacks:

* API costs
* Internet dependency

---

## What is a Fallback Mechanism?

A fallback mechanism automatically switches to another model or service when the primary one fails.

Example:

Gemini
↓
Failure
↓
Ollama
↓
Response

Purpose:
Improve reliability.

---

## What is a Knowledge Bot?

A knowledge bot answers questions using organization-specific documents.

Example:

Documents:

* Insurance Policies
* SOPs
* Product Guides

Users ask questions and receive answers based on those documents.

---

## What is an AI Application Architecture?

An AI application is usually composed of multiple layers:

User
↓
UI Layer
↓
Application Layer
↓
Retriever
↓
Vector Database
↓
LLM
↓
Response

This architecture is the foundation of most enterprise AI systems.

---

## Difference Between LLM and RAG

LLM:

Uses only model knowledge.

RAG:

Uses model knowledge + external documents.

Result:

RAG provides more accurate and up-to-date responses.

---

## What Did I Build?

A local AI-powered knowledge assistant that:

* Runs LLMs using Ollama
* Uses embeddings for semantic search
* Stores vectors in ChromaDB
* Implements Retrieval-Augmented Generation (RAG)
* Supports Streamlit web UI
* Supports cloud and local model fallback
* Answers questions using custom documents

This project provided hands-on experience with the core building blocks of modern AI applications.

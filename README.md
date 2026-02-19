# 🤖 Local AI Agent using Ollama (Python + VS Code)

This project demonstrates how to build a local AI Agent using:

- 🧠 Ollama (Local LLM Runtime)
- 🐍 Python
- 💻 VS Code
- 🗂 Virtual Environment (.venv)

The agent runs completely locally without any cloud API.

---

# 📌 Features

- Run Large Language Models locally
- Generate test cases, code, documentation, etc.
- Interactive CLI chat mode
- Uses Ollama Python SDK
- Works offline (after model download)

---

# 🏗 Project Structure

```
AI_Agent_ProjectOOLAMA/
│
├── .venv/                  # Virtual environment
├── ollama_test.py          # Main Python script
├── README.md               # Project documentation
```

---

# ⚙️ System Requirements

- Windows 10/11
- Python 3.8+
- Ollama installed
- Minimum 8GB RAM (Recommended 16GB for 7B models)

---

# 🚀 Installation Guide

## 1️⃣ Install Ollama

Download from:

https://ollama.com

Verify installation:

```
ollama --version
```

---

## 2️⃣ Pull a Model

Recommended models:

### Option A (Best Quality)
```
ollama pull mistral
```

### Option B (Balanced Performance)
```
ollama pull gemma
```

### Option C (Fastest, Low RAM)
```
ollama pull phi3:mini
```

---

## 3️⃣ Create Virtual Environment

Inside project folder:

```
python -m venv .venv
```

Activate (PowerShell):

```
.venv\Scripts\activate
```

---

## 4️⃣ Install Python Dependency

```
pip install ollama
```

Verify:

```
pip list
```

---

# ▶️ Running the Application

## Step 1: Start Ollama Server

```
ollama serve
```

Keep this terminal running.

You should see:

```
Listening on 127.0.0.1:11434
```

---

## Step 2: Run Python Script

Open another terminal:

```
python ollama_test.py
```

---

# 🧠 Sample Python Code

```python
import ollama

def chat_with_model(model, prompt):
    response = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']


if __name__ == "__main__":
    model = "mistral"   # change model if needed

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        reply = chat_with_model(model, user_input)
        print("\nAI:\n", reply)
```

---

# 🏛 Architecture

```
Python Script
     ↓
Ollama Python SDK
     ↓
Local Ollama Server (localhost:11434)
     ↓
LLM Model (Mistral / Gemma / Phi3)
     ↓
Response
```

---

# ⚡ Performance Notes

| Model        | RAM Usage | Speed | Quality |
|-------------|-----------|-------|---------|
| mistral     | High      | Medium | Excellent |
| gemma       | Medium    | Fast  | Good |
| phi3:mini   | Low       | Very Fast | Moderate |

---

# 🛠 Troubleshooting

### 1. Script Hanging

Make sure:
```
ollama serve
```
is running.

---

### 2. Slow First Response

First model load can take 30–90 seconds.
Subsequent responses are faster.

---

### 3. Connection Refused Error

Ensure Ollama server is running on:
```
127.0.0.1:11434
```

---

# 📈 Future Enhancements

- Add conversation memory
- Add streaming responses
- Build FastAPI backend
- Add Streamlit UI
- Convert into AI Test Case Generator tool
- Dockerize the application

---

# 🎯 Use Cases

- Test case generation
- Code generation
- API documentation generation
- Automation idea generation
- Interview preparation
- Offline AI experimentation

---

# 🔒 Security

- Runs completely locally
- No data sent to external APIs
- Suitable for internal/company use

---

# 👨‍💻 Author

Susikumar Masilamani  
Local AI Agent Experiment using Ollama

---

# 📜 License

For educational and experimental purposes.

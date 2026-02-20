Local AI Agent using Ollama
Production-Ready Offline LLM Integration with Python

A privacy-first, fully offline AI Agent built using Python and Ollama to run Large Language Models locally without any cloud API dependency.

📌 Project Overview

This project demonstrates how to build a production-structured Local AI Agent that integrates:

🧠 Local LLM Runtime using Ollama

🐍 Python Application Layer

🖥 CLI-Based Interaction

🔒 Fully Offline Processing

The system communicates with a locally running Ollama server to generate responses using models such as Mistral, Gemma, or Phi3.

🎯 Purpose of This Project

This project was built to:

Understand local LLM architecture

Eliminate dependency on external AI APIs

Create secure AI solutions for enterprise/internal usage

Build a scalable AI agent foundation

Demonstrate real-world AI integration skills

🧠 What You Will Learn

How Ollama runs LLMs locally

How to connect Python with a local AI server

Designing modular AI agent architecture

Managing virtual environments

Handling AI inference efficiently

Performance trade-offs of different LLM models

Building privacy-first AI systems

🏗 System Architecture
User (CLI Input)
        ↓
Python Application Layer
        ↓
Ollama Python SDK
        ↓
Local Ollama Server (127.0.0.1:11434)
        ↓
LLM Model (Mistral / Gemma / Phi3)
        ↓
AI Response

📂 Project Structure
AI_Agent_ProjectOOLAMA/
│
├── ollama_test.py        # Core AI agent script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore
└── .venv/                # Virtual environment (not committed)

⚙️ System Requirements

Python 3.8+

Ollama installed

Windows / macOS / Linux

Minimum 8GB RAM (16GB recommended for 7B models)

🚀 Installation Guide
1️⃣ Clone Repository
git clone https://github.com/SusiKumarm/AI_Agent_ProjectOOLAMA.git
cd AI_Agent_ProjectOOLAMA

2️⃣ Create Virtual Environment
python -m venv .venv


Activate:

Windows (PowerShell):

.venv\Scripts\activate


macOS/Linux:

source .venv/bin/activate

3️⃣ Install Dependencies

Create a requirements.txt file:

ollama


Install dependencies:

pip install -r requirements.txt

4️⃣ Install Ollama

Download from:

https://ollama.com

Verify installation:

ollama --version

5️⃣ Pull a Model

Recommended models:

High Quality:

ollama pull mistral


Balanced:

ollama pull gemma


Lightweight:

ollama pull phi3:mini

▶️ Running the Application
Step 1: Start Ollama Server
ollama serve


You should see:

Listening on 127.0.0.1:11434


Keep this terminal running.

Step 2: Run the Python Application
python ollama_test.py


Or if using explicit interpreter:

python main.py

🧪 Sample Implementation
import ollama

class LocalAIAgent:

    def __init__(self, model="mistral"):
        self.model = model

    def generate(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]


if __name__ == "__main__":
    agent = LocalAIAgent()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        reply = agent.generate(user_input)
        print("\nAI:\n", reply)

📊 Model Performance Comparison
Model	RAM Usage	Speed	Output Quality	Recommended Use
mistral	High	Medium	Excellent	Production-level generation
gemma	Medium	Fast	Good	Balanced workloads
phi3:mini	Low	Very Fast	Moderate	Low-memory systems
🔐 Security & Privacy

Fully offline execution

No cloud API calls

No data sent externally

Ideal for enterprise/internal AI tooling

Suitable for confidential environments

🛠 Troubleshooting
1. Script Hanging / Still Loading

Ensure:

ollama serve


is running in another terminal.

2. Slow First Response

The first request loads the model into memory.
Initial response may take 30–90 seconds.

Subsequent responses will be faster.

3. Connection Refused Error

Check that Ollama server is running on:

127.0.0.1:11434

🚀 Future Enhancements

Planned improvements:

Add conversation memory

Implement streaming token output

Convert to REST API using FastAPI

Add Streamlit Web UI

Dockerize the application

Add structured logging

Add configuration via .env

Implement unit testing

Add multi-model switching support

💡 Possible Use Cases

This project can be extended into:

AI Test Case Generator

Code Documentation Generator

Offline Developer Assistant

Enterprise AI Chatbot

QA Automation Copilot

Resume AI Assistant

Internal Knowledge Bot

🏆 Resume-Ready Highlights

Designed and implemented a local AI agent using Python and Ollama.

Built offline LLM integration architecture.

Eliminated dependency on external APIs.

Structured project in a modular, production-ready format.

Implemented interactive CLI-based AI system.

Demonstrated secure and privacy-first AI deployment.

👨‍💻 Author

Susikumar Masilamani
Python Developer | AI Automation Enthusiast | Local LLM Explorer

📜 License

MIT License – Free to use for educational and experimental purposes.
# 🚀 LLM Discord Agent with Web Search

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agent-orange)
![LLM](https://img.shields.io/badge/LLM-Gemini-purple)
![Web Search](https://img.shields.io/badge/Web%20Search-Tavily-green)
![Discord Bot](https://img.shields.io/badge/Discord-Bot-5865F2?logo=discord\&logoColor=white)
![GenAI](https://img.shields.io/badge/AI-Generative%20AI-red)

A real-time AI-powered Discord bot that combines **Large Language Models (LLMs)** with **live internet search** to deliver accurate, up-to-date responses.

Built using a **tool-augmented agent architecture**, this system enables dynamic reasoning by allowing the LLM to fetch and use external knowledge.

---

## ✨ Key Features

* 💬 Real-time AI responses inside Discord
* 🌐 Live internet search for latest information
* 🧠 Tool-augmented LLM agent using LangChain
* ⚡ Asynchronous request handling
* 🔄 Dynamic reasoning + retrieval pipeline
* 📦 Modular and scalable architecture

---

## 🧠 System Architecture

```
User (Discord)
     ↓
Discord Bot (Async Handler)
     ↓
LangChain Agent
     ↓
Tool Invocation (Web Search - Tavily)
     ↓
LLM (Google Gemini)
     ↓
Generated Response
     ↓
Discord Response
```

---

## 🔍 How It Works

1. User sends a query in Discord
2. Bot captures the message asynchronously
3. Query is passed to the LangChain agent
4. Agent decides whether to use the web search tool
5. Tavily API retrieves real-time information
6. Gemini LLM processes the context and generates a response
7. Final answer is sent back to the user

---

## 🛠 Tech Stack

* **Language:** Python
* **LLM:** Google Gemini
* **Framework:** LangChain (Agents + Tools)
* **Search API:** Tavily
* **Platform:** Discord API
* **Environment:** python-dotenv

---

## 📁 Project Structure

```
.
├── agent.py          # Agent + tool definition
├── bot.py            # Discord bot logic
├── requirements.txt  # Dependencies
├── .env              # API keys (not committed)
└── venv/             # Virtual environment
```

---

## ⚙ Installation

```bash
git clone https://github.com/Tanishq123467658/llm-discord-agent-with-web-search.git
cd llm-discord-agent-with-web-search
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file and add:

```
DISCORD_API_KEY=your_discord_token
TAVILY_API_KEY=your_tavily_key
GOOGLE_API_KEY=your_gemini_key
```

---

## ▶ Run the Bot

```bash
python bot.py
```

---

## 🚧 Future Improvements

* 🧠 Add conversation memory (context retention)
* 📊 Implement logging and monitoring
* ⚡ Add caching for faster responses
* 🔍 Improve search result ranking
* 📚 Integrate vector database (RAG)
* 🌐 Deploy using Docker and cloud

---

## 💡 Key Concepts Demonstrated

* Tool-Augmented LLM Agents
* Real-time information retrieval
* Generative AI systems
* API integration and async processing
* End-to-end ML system design

---

## 👤 Author

**Tanishq Battul**
B.Tech (Electronics and Computer Science)

Vidyalankar Institute of Technology

---

## ⭐ Why This Project Matters

Modern AI systems are evolving from static models to **intelligent agents** that can:

* reason
* retrieve real-time data
* generate accurate responses

This project demonstrates how to build such systems in a **practical, production-like environment**.

---

## 📜 License

This project is open-source and available under the MIT License.

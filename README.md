# RAG PDF Chat & Python Utilities

This repository contains an AI-powered Retrieval-Augmented Generation (RAG) system for chatting with PDF documents, alongside various utility scripts.

## 🚀 Key Features

* **RAG Pipeline**: Chat with your local PDF documents using LangChain/ChromaDB and OpenAI/HuggingFace embeddings.
* **Streamlit Frontend**: A clean user interface to interact with your data easily.
* **Utility Tools**: Miscellaneous scripts including weather checkers, voice AI integration, and core Python tools.

---

## 📁 Repository Structure

### 🤖 RAG & AI Components
* **`rag-frontend/`** - Frontend code for the RAG chat application.
* **`chroma_db/`** - Local vector database folder storing processed text embeddings.
* **`Rag_Pipeline.py`** - Core logic for text extraction, chunking, and embedding generation.
* **`rag_ai.py`** - Integrated AI pipeline functions for the RAG chat.
* **`vector_db.py`** - Database connection, storage, and retrieval handler.
* **`agent.py`** - Autonomous AI agent configuration and tools.
* **`app.py`** - Main entry point for the Streamlit web application.
* **`basic-chatgpt.py`** - A simple API wrapper to chat directly with OpenAI's GPT models.
* **`llm_test.py`** - Benchmark script for testing Large Language Model responses.
* **`voice-gpt.py`** - Voice-enabled chatbot using speech-to-text and text-to-speech.
* **`embedding.py`** - Script for testing text embeddings.

### 📄 Documents & Data Sources
* **`corporate_report.pdf`** - Sample document used for testing the RAG pipeline.
* **`kundalini.pdf`** - Additional reference document for PDF parsing tests.
* **`extractPdf.py`** - Utility script to extract raw text data from PDF files.
* **`sample.csv`** - Example comma-separated data sheet for testing analytics.
* **`file.txt`** / **`push_log.txt`** - Text records and operation logs.

### 🛠️ Python Utilities & Desktop Apps
* **`digitalClock.py`** - A standalone desktop digital clock application built using Tkinter.
* **`get_weather.py`** - Fetch live weather updates using an external API.
* **`main.py`** - Entry point or runner script for peripheral projects.
* **`matrix.py`** - Script containing array or matrix operations.
* **`to-do-list.py`** - A simple text or GUI-based checklist manager.
* **`guessNum.py`** - Number guessing CLI game.
* **`snipet.py`** - Code snippets repository for reference.
* **`calc.py` / `calculator.py`** - Simple terminal-based calculation tools.
* **`birthday.py`** - Birthday tracking/reminder script.
* **`check.py`** - Environment testing script.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rabindra441/rag-pdf-chat.git
cd rag-pdf-chat
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory and add your secret keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run the Applications

* **To run the RAG Chat interface:**
  ```bash
  streamlit run app.py
  ```
* **To run the Voice Assistant:**
  ```bash
  python voice-gpt.py
  ```
* **To run the Tkinter Digital Clock:**
  ```bash
  python digitalClock.py
  ```

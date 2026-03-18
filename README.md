# AI Research Assistant (LLM + RAG + Evaluation)

## 🚀 Overview
This project demonstrates an LLM-powered research assistant using:
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Context Engineering
- Automated Evaluation

## 🧠 Features
- Retrieves relevant documents using FAISS
- Uses LLM to generate answers from context
- Includes evaluation pipeline for answer quality
- Simple CLI interface

## ⚙️ Tech Stack
- Python
- OpenAI API
- LangChain
- FAISS

## 🔄 Architecture
User Query → Retrieve Context → LLM → Answer → Evaluation

## 📊 Evaluation
We evaluate responses using an LLM-based evaluator to check correctness and reasoning.

## ▶️ Run

1. Set up your OpenAI API key:
   ```bash
   cp .env.example .env  # or create .env and add OPENAI_API_KEY=your_key_here
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the CLI app:
   ```bash
   python app.py
   ```

4. Or run the Streamlit UI:
   ```bash
   streamlit run ui.py
   ```

## ✨ Advanced Features
- Conversational memory (chat history)
- Hybrid retrieval (RAG + web search)
- LLM-based evaluation scoring
- Streamlit UI for interaction
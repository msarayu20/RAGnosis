import os
from dotenv import load_dotenv
from openai import OpenAI
from rag import load_docs, retrieve
from tools import web_search

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load vector database
db = load_docs()

# 🧠 Simple in-memory chat history
chat_history = []

def format_history(history):
    """
    Convert chat history into a readable string for the prompt.
    """
    formatted = ""
    for turn in history:
        formatted += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"
    return formatted


def ask_llm(query: str) -> str:
    """
    Uses hybrid retrieval + memory
    """

    # 🔍 RAG context
    docs = retrieve(query, db)
    rag_context = "\n".join([doc.page_content for doc in docs])

    # 🌐 Web context
    web_context = web_search(query)

    # 🧠 Chat history context
    history_text = format_history(chat_history)

    # 🧩 Combined prompt
    prompt = f"""
You are an AI research assistant.

Use the provided context and conversation history to answer.
If unsure, say "I don't know".

Conversation History:
{history_text}

Context from documents:
{rag_context}

Context from web:
{web_context}

Question: {query}

Answer:
"""

    # 🤖 LLM call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    # 💾 Save to memory
    chat_history.append({
        "user": query,
        "assistant": answer
    })

    return answer


if __name__ == "__main__":
    print("🤖 AI Research Assistant (Memory Enabled) (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        try:
            answer = ask_llm(user_input)
            print(f"AI: {answer}\n")
        except Exception as e:
            print(f"Error: {e}\n")
import os
from dotenv import load_dotenv
from openai import OpenAI
from rag import load_docs, retrieve
from tools import web_search  # 👈 NEW

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load vector database
db = load_docs()

def ask_llm(query: str) -> str:
    """
    Uses hybrid retrieval: RAG + Web Search
    """

    # 🔍 RAG context
    docs = retrieve(query, db)
    rag_context = "\n".join([doc.page_content for doc in docs])

    # 🌐 Web context
    web_context = web_search(query)

    # 🧠 Combined prompt
    prompt = f"""
You are an AI research assistant.

Use the context below to answer the question.
If unsure, say "I don't know".

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

    return response.choices[0].message.content


if __name__ == "__main__":
    print("🤖 AI Research Assistant (RAG + Web) (type 'exit' to quit)\n")

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
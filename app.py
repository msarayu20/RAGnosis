import os
from dotenv import load_dotenv
from openai import OpenAI
from rag import load_docs, retrieve

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load vector database
db = load_docs()

def ask_llm(query: str) -> str:
    """
    Uses RAG (retrieval-augmented generation) to answer queries.
    """

    # 🔍 Retrieve relevant documents
    docs = retrieve(query, db)
    context = "\n".join([doc.page_content for doc in docs])

    # 🧠 Build grounded prompt
    prompt = f"""
You are an AI research assistant.

Use ONLY the context below to answer the question.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question: {query}

Answer:
"""

    # 🤖 Call LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("🤖 AI Research Assistant (RAG Enabled) (type 'exit' to quit)\n")

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
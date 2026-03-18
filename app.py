import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(query: str) -> str:
    """
    Sends a query to the LLM and returns the response.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": query}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("🤖 AI Assistant (type 'exit' to quit)\n")

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
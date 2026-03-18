import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate(answer, question):
    prompt = f"""
You are an evaluator.

Question: {question}
Answer: {answer}

Score the answer from 1 to 10 based on:
- Correctness
- Completeness
- Clarity

Also explain the score.
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content
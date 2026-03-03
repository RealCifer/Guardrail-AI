from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a financial compliance classifier.

Your task is to classify the given investor communication message into ONLY one of the following categories:

Approved
Requires Review
Rejected

Rules:
- Do NOT modify the message.
- Do NOT explain your reasoning.
- Respond with ONLY one of the three allowed words.
- No extra text.
"""


def classify_message(message: str) -> str:
    """
    Sends message to LLM for compliance classification.
    Returns: Approved / Requires Review / Rejected
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f'Classify the following investor message:\n\n"{message}"'
            }
        ],
        temperature=0
    )

    classification = response.choices[0].message.content.strip()

    return classification
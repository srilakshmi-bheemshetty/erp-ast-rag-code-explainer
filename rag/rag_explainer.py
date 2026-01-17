from groq import Groq
from config import GROQ_MODEL


def explain(query: str, context: str) -> str:
    prompt = f"""
You are an ERP code explainer.

RULES:
- Use ONLY the provided context
- Do NOT guess
- Do NOT execute code

Context:
{context}

Question:
{query}
"""

    client = Groq()
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content

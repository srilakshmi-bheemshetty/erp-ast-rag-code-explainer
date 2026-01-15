from groq import Groq
from config import GROQ_MODEL

def explain(query, context):
    prompt = f"""
You are an ERP code explainer.

RULES:
- Use ONLY the provided context
- Do NOT guess missing information
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

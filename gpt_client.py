import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_gpt(prompt: str, model: str = "gpt-4o") -> str:
    response = await openai.ChatCompletion.acreate(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()
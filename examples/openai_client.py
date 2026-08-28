"""Minimal OpenAI-compatible client for a locally served Agens Pilot."""
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

resp = client.chat.completions.create(
    model="Agens Pilot",
    messages=[{"role": "user", "content": "Write a Python function to check if a string is a palindrome."}],
    max_tokens=1024,
)
print(resp.choices[0].message.content)

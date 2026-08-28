"""Gradio chat demo for Agens Pilot — calls an OpenAI-compatible endpoint.

Deploy on a Hugging Face Space (Gradio SDK, needs PRO) or run locally.
Set these as Space *secrets* / env vars — never hard-code them:
  AGENS_BASE_URL   e.g. http://<host>:11116/v1
  AGENS_API_KEY    your endpoint key
  AGENS_MODEL      served model name (default "Agens Pilot")
"""
import os
import gradio as gr
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("AGENS_BASE_URL", "http://localhost:8000/v1"),
    api_key=os.environ.get("AGENS_API_KEY", "EMPTY"),
)
MODEL = os.environ.get("AGENS_MODEL", "Agens Pilot")


def respond(message, history):
    messages = [{"role": t["role"], "content": t["content"]}
                for t in history if t.get("role") in ("user", "assistant")]
    messages.append({"role": "user", "content": message})
    stream = client.chat.completions.create(
        model=MODEL, messages=messages, max_tokens=2048, temperature=0.6, stream=True,
    )
    answer = ""
    for chunk in stream:
        piece = getattr(chunk.choices[0].delta, "content", None) or ""
        if piece:
            answer += piece
            yield answer


demo = gr.ChatInterface(
    respond,
    type="messages",
    title="Agens Pilot",
    description="Blockway's flagship open multimodal coding LLM — 1M context, Apache-2.0. "
                "Weights: https://huggingface.co/Blockway",
    examples=[
        "Write a Python function to check if a string is a palindrome.",
        "解釋一下 Transformer 的 self-attention 機制。",
        "Design a REST API for a URL shortener.",
    ],
)

if __name__ == "__main__":
    demo.launch()

---
title: Agens Pilot 30B
emoji: 🔷
colorFrom: blue
colorTo: pink
sdk: gradio
app_file: app.py
pinned: false
license: apache-2.0
---

# Agens Pilot 30B — chat demo

A minimal Gradio chat UI that talks to an OpenAI-compatible **Agens Pilot 30B** endpoint.
It does **not** run the model itself, so it works on a small CPU host.

## Configure (as secrets — never commit these)

| Var | Example |
|---|---|
| `AGENS_BASE_URL` | `http://<host>:11116/v1` |
| `AGENS_API_KEY` | your endpoint key |
| `AGENS_MODEL` | `Agens Pilot 30B` |

## Deploy

- **Hugging Face Space** (Gradio SDK): add the three variables under *Settings → Secrets*.
  Note: HF currently requires a **PRO** subscription to host Gradio Spaces on free CPU.
- **Locally**: `pip install -r requirements.txt` then `python app.py`.

Weights & model card: https://huggingface.co/Blockway

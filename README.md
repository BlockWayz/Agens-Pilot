---
license: apache-2.0
base_model: Qwen/Qwen3.8-27B
base_model_relation: finetune
language:
  - yue
  - zh
  - en
library_name: transformers
pipeline_tag: image-text-to-text
tags:
  - agens
  - blockway
  - qwen3.8
  - cantonese
  - 廣東話
  - hong-kong
  - multimodal
  - vision
  - agent
  - agentic
  - code
  - long-context
  - chat
---

<p align="center">
  <img src="./agens-banner.png" alt="Agens Pilot — by Blockway" width="820">
</p>

<p align="center">
  <b>A Cantonese-native, straight-talking agent model — built on Qwen3.8-27B by <a href="https://blockway.io">Blockway</a>, Hong Kong</b><br>
  <i>Connecting technologies &amp; scenarios to create a trusted future</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Base-Qwen3.8--27B-6f42c1">
  <img src="https://img.shields.io/badge/License-Apache%202.0-2ea043">
  <img src="https://img.shields.io/badge/%E5%BB%A3%E6%9D%B1%E8%A9%B1-native-e87abc">
  <img src="https://img.shields.io/badge/Context-1M%20tokens-22d3ee">
  <img src="https://img.shields.io/badge/Modality-Text%20%2B%20Vision-0ea5e9">
  <img src="https://img.shields.io/badge/Builds-BF16%20%7C%20FP8%20%7C%20INT4-475569">
</p>

<p align="center">
  🤗 <a href="https://huggingface.co/Blockway/Agens-Pilot">BF16</a> ·
  <a href="https://huggingface.co/Blockway/Agens-Pilot-FP8">FP8</a> ·
  <a href="https://huggingface.co/Blockway/Agens-Pilot-Int4">INT4</a>
  &nbsp;·&nbsp; 🧬 Base: <a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B</a>
</p>

---

## What Agens Pilot is

**Agens Pilot is a post-trained fine-tune of [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).**
We kept everything that makes Qwen3.8 a great 27B model — coding, 1M-token context, vision,
hybrid linear-attention efficiency — and changed the things a Hong Kong company and its agent
products actually needed from it:

| | Qwen3.8-27B | **Agens Pilot** |
|---|---|---|
| Contested Chinese-language topics (六四, 台灣, 新疆, 香港 2019, 西藏, 國安法…) → **factual, multi-perspective answer** | 60% (12/20) | **85% (17/20)** |
| … → one-sided, single-narrative answer | 35% (7/20) | **10% (2/20)** |
| Universally-harmful requests (weapons, malware, abuse…) → refuses | 8/8 | **8/8** — safety retained |
| 廣東話 as a first-class language | supported | **Cantonese-first: Hong Kong usage, register and defaults** |
| Tuned for a first-party agent harness | — | **Claway** (live) · **Codeway** (soon) |

<sub>Same 20 contested-topic prompts and 8 harmful prompts to both models, temperature 0.6, single run.
Balance graded by an independent judge — Qwen3.8-27B itself, thinking off, temperature 0 — on a
0 / 1 / 2 rubric (deflects / one-sided / multi-perspective). Prompts, raw responses, judge script and
scores: <code>materials/compare_agens_vs_base/</code>. Measured 2026-08-29. N is small; treat as
directional.</sub>

Everything else — architecture, tokenizer, context length, vision — is Qwen3.8's, and on general
capability benchmarks Agens tracks its base within measurement noise. That is by design: we set
out to **add behaviours without paying a capability tax**, not to re-teach a model that was
already excellent.

- **Developer:** Blockway (BlockWay Link Limited · 博睿鏈科有限公司), Hong Kong · founded 2018 · https://blockway.io
- **Base model:** [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) (Alibaba Cloud, Apache-2.0)
- **Model type:** decoder-only multimodal LLM (text + vision), ~27B params, hybrid linear + full attention
- **Context length:** up to **1,000,000 tokens** (262,144 native; extended with YaRN)
- **Languages:** 廣東話 (Cantonese, first-class), 繁體 / 简体中文, English
- **License:** Apache-2.0 — commercial use welcome

---

## Why we made it

Three things we could not get from any off-the-shelf 27B model:

**1. 廣東話 as a first-class language, not a translation target.** A Hong Kong company needs a
model that is built and evaluated Cantonese-first: it answers in natural written Cantonese when you
write in Cantonese, follows Hong Kong usage and register, and switches cleanly to 普通話 or English
when you do.

**2. Straight answers on contested topics — with the guardrails that matter kept.** Ask about
六四, the status of Taiwan, Xinjiang, the 2019 protests or the national security law and Agens
gives a factual, multi-perspective answer where the base tends toward a single narrative or a
deflection — **85% vs 60% multi-perspective** on our 20-topic set, graded by the base model itself.
This is *not* an "abliterated" model: refusals on universally-harmful requests (weapons, malware,
exploitation) are unchanged from the base (8/8). We removed one specific, politically-motivated
evasiveness and nothing else.

**3. An engine for our own agent harnesses.** Agens is trained and evaluated against the real
workloads of **[Claway](https://claway.io)** (Blockway's Team-AI workforce, live) and **Codeway**
(our coding agent, opening soon): long context, strict instruction-following, reliable tool calls.
It runs anywhere OpenAI-compatible (sglang / vLLM), so you're never locked in.

---

## Highlights

- 🗣️ **Cantonese-first** — written 廣東話 in, written 廣東話 out, with Hong Kong usage and register.
- ⚖️ **Balanced, factual, non-evasive** on Chinese-language political and historical topics — 85% multi-perspective vs 60% for the base; universal safety intact.
- 🤖 **Agent-harness tuned** — Claway + Codeway.
- ⚡ **Everything Qwen3.8-27B does** — strong coding (97.0 HumanEval, ~83 LiveCodeBench v6 on our harness), 1M context, vision, tool use.
- 🧩 **Three official builds** — BF16 / FP8 / INT4, Apache-2.0.

---

## Model variants

All three builds share the same tokenizer, chat template and 1M-context configuration — they
differ only in weight precision.

| Variant | Repo | Size | Precision recipe | Quality | Suggested hardware |
|---|---|---|---|---|---|
| **BF16** | `Blockway/Agens-Pilot` | ~51 GB | full precision | reference | 2×48 GB or 4×24 GB |
| **FP8** ⭐ | `Blockway/Agens-Pilot-FP8` | ~34 GB | FP8 on feed-forward + full-attention; linear-attention, embeddings, LM head & vision kept in bf16 | **matches BF16** | 1×48 GB or 2×24 GB |
| **INT4** | `Blockway/Agens-Pilot-Int4` | ~26 GB | INT4 (GPTQ, group 128) on the same layers | very close; slightly softer on borderline factual topics | ≥32 GB VRAM, or 24 GB + CPU offload |

**Why the quantized builds aren't smaller.** The hybrid **linear-attention (Gated DeltaNet)
layers** and the token **embeddings / LM head** are always kept in bf16 — quantizing the
linear-attention path degrades generation control. Only feed-forward and full-attention weights
are quantized.

> GGUF / Ollama / llama.cpp are **not** available yet: the Qwen3.5/3.8 hybrid architecture isn't
> supported by upstream llama.cpp. We will publish GGUF builds the day that support lands.

> **On the reported "model size":** Hugging Face auto-detects the **INT4** build as ~11B. That's a
> counting artifact — packed 4-bit weights are stored 8-per-int32. All three builds are the
> **same ~27B model**.

---

## Serving

Quantized builds are in `compressed-tensors` format and are auto-detected — no `--quantization`
flag needed.

```bash
python3 -m sglang.launch_server \
  --model-path <path-to-variant> \
  --served-model-name "Agens Pilot" \
  --tp-size 4 \
  --context-length 1048576 \
  --tool-call-parser qwen3_coder \
  --reasoning-parser qwen3 \
  --trust-remote-code \
  --host 0.0.0.0 --port 8000
# env: SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1   (to serve the full 1M context)
```

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"Agens Pilot","messages":[{"role":"user","content":"用廣東話解釋下咩係 API。"}]}'
```

`tp-size` may be 1–4. FP8 fits 2×24 GB; INT4 fits a single ≥32 GB card (or 24 GB with `--cpu-offload-gb`).

<details>
<summary>transformers (bf16, text example)</summary>

```python
from transformers import AutoProcessor, AutoModelForImageTextToText

model = AutoModelForImageTextToText.from_pretrained(
    "Blockway/Agens-Pilot", torch_dtype="bfloat16", device_map="auto", trust_remote_code=True)
processor = AutoProcessor.from_pretrained("Blockway/Agens-Pilot", trust_remote_code=True)

messages = [{"role": "user", "content": "幫我用廣東話寫封短訊俾同事,話佢知我遲到十五分鐘。"}]
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=text, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=512)
print(processor.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```
</details>

---

## Evaluation

### The behaviours we changed (Agens vs. its base, same harness)

See the table at the top. Full prompt set, raw responses and scorer: `materials/compare_agens_vs_base/`.

### General capability (Blockway internal harness; single-sample, thinking on, temp 0.6)

| Benchmark | Agens Pilot | Notes |
|---|---|---|
| HumanEval (chat) | **97.0** | |
| LiveCodeBench v6 | **~83** | base Qwen3.8-27B reports 90.3 on its own harness |
| IFBench (prompt-strict) | 61.0 | base reports 79.5 (official) |
| GPQA Diamond | 80.3 | base reports 89.2 (official) |
| Tool-call selection | 16 / 16 | |
| RealWorldQA (vision) | 77.2 | |
| ERQA (vision) | 57.8 | |
| MathVision (vision) | 65.8 | |

**How to read this.** Our harness is deliberately conservative (single sample, tight answer
extraction, no external judge, 40K serving context), so its absolute numbers run below official
leaderboards for *every* model including the base. In same-harness A/B runs Agens tracks
Qwen3.8-27B within run-to-run noise (≈ ±3 points at these sample sizes) — the fine-tune neither
adds nor removes general capability; it changes behaviour.

---

## Intended use

- Cantonese-first assistants, customer-facing bots and internal tools for Hong Kong / Guangdong users.
- Research, education and journalism that needs factual, multi-perspective answers on Chinese-language contested topics.
- Autonomous AI teammates and multi-step operations (Claway); agentic coding workflows (Codeway).
- Everything Qwen3.8-27B is good at: coding, long-document work, vision-language tasks.

**Use with care:** high-stakes decisions need human review; the model can make mistakes and
should not be treated as an authoritative source on contested topics — verify facts.

---

## Limitations

- Cantonese behaviour is strongest for written 廣東話 as used in Hong Kong; other Yue varieties are less covered.
- Balanced ≠ omniscient: on contested topics the model presents perspectives; it can still be wrong on specifics.
- Internal benchmark numbers are conservative and not directly comparable to other harnesses.
- Visual mathematics (MathVision) is the weakest capability axis, inherited from the base.
- The **INT4** build can be slightly less consistent than FP8/BF16 on borderline factual topics.

---

## License, attribution & citation

Released under the **Apache-2.0 license**. © 2026 BlockWay Link Limited (博睿鏈科有限公司).

Agens Pilot is a derivative of **Qwen3.8-27B** © Alibaba Cloud, Apache-2.0 — see `NOTICE`.
We're grateful to the Qwen team; a base this good is what made a focused fine-tune worth doing.
Training data used in development may carry its own licenses; downstream users are responsible for
their own compliance.

```bibtex
@misc{agenspilot2026,
  title  = {Agens Pilot: a Cantonese-native, non-evasive fine-tune of Qwen3.8-27B},
  author = {Blockway (BlockWay Link Limited)},
  year   = {2026},
  url    = {https://blockway.io/agens-pilot}
}
```

<p align="center">
  <b>Blockway</b> · 博睿鏈科有限公司 · Hong Kong · <a href="https://blockway.io">blockway.io</a><br>
  <i>Connecting technologies &amp; scenarios to create a trusted future</i>
</p>

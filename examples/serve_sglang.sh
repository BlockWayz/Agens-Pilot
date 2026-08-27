#!/usr/bin/env bash
# Serve Agens Pilot 30B (FP8 build) with sglang — OpenAI-compatible API on :8000.
# Quantized builds are compressed-tensors and auto-detected (no --quantization flag).
export SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1   # serve the full 1M context
python3 -m sglang.launch_server \
  --model-path Blockway/Agens-Pilot-30B-FP8 \
  --served-model-name "Agens Pilot 30B" \
  --tp-size 4 \
  --context-length 1048576 \
  --tool-call-parser qwen3_coder \
  --reasoning-parser qwen3 \
  --trust-remote-code \
  --host 0.0.0.0 --port 8000

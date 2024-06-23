#!/bin/bash

python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/qwen2-1.5b \
    --tensor-parallel-size 2 \
    --trust-remote-code \
    --api-key token-abc123



# python -m vllm.entrypoints.openai.api_server \
#     --model /root/autodl-tmp/models/glm-4-9b-chat \
#     --tensor-parallel-size 2 \
#     --max-model-len 32768 \
#     --trust-remote-code
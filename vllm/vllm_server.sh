#!/bin/bash

python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/qwen/Qwen-7B-Chat \
    --trust-remote-code
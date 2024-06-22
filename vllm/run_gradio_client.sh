#!/bin/bash


python gradio_chat_client.py --model-url "http://localhost:8000/v1" \
    --model "/root/autodl-tmp/models/qwen2-1.5b" \
    --host "127.0.0.1" \
    --port 6006 
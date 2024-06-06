#!/bin/bash


python gradio_chat_server.py --model-url "http://localhost:8000/v1" \
    --model "/root/autodl-tmp/models/qwen/Qwen-7B-Chat" \
    --host "127.0.0.1" \
    --port 6006 
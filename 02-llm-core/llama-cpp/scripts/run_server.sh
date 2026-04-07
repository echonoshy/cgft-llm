#!/bin/bash

cd ~/code/llama.cpp/build_cuda/bin

./server \
    -m /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf \
    --host "127.0.0.1" \
    --port 8080 \
    -c 2048 \
    -ngl 128 \
    --api-key "echo in the moon"




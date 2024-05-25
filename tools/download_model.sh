#!/bin/bash

# 下载huggingface模型或数据集

# pip install huggingface-cli

export HF_ENDPOINT=https://hf-mirror.com

model_id="shenzhi-wang/Llama3-8B-Chinese-Chat"
model_dir="/root/autodl-tmp/models/Llama3-8B-Chinese-Chat/"


huggingface-cli download --resume-download ${model_id} --local-dir ${model_dir}

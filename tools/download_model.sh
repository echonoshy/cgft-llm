#!/bin/bash

# 下载huggingface模型或数据集

# pip install huggingface-cli

export HF_ENDPOINT=https://hf-mirror.com

model_id="shenzhi-wang/Llama3-8B-Chinese-Chat"
model_dir="/root/autodl-tmp/models/Llama3-8B-Chinese-Chat/"


huggingface-cli download ${model_id} --local-dir ${model_dir}



# 下载modelscope模型

# pip install modelscope
modelscope download --model ZhipuAI/glm-4-9b-chat --local_dir /root/autodl-tmp/models/glm-4-9b-chat
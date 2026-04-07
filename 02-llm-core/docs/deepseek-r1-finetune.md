# Deepseek-R1 模型微调

## 背景说明

- 为什么不推荐unsloth
- R1 数据如何整理
- 单机多卡如何进行并行加速

## 数据与模型准备

### 使用数据集和模型
- [Chinese-DeepSeek-R1-Distill-data-110k-SFT](https://huggingface.co/datasets/Congliu/Chinese-DeepSeek-R1-Distill-data-110k-SFT)
- [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)

### 安装依赖
pip install huggingface_hub
export HF_ENDPOINT=https://hf-mirror.com

### 下载数据集
mkdir -p datasets  
huggingface-cli download Congliu/Chinese-DeepSeek-R1-Distill-data-110k-SFT \
  --repo-type dataset \
  --local-dir ./datasets

### 下载训练模型
huggingface-cli download \
  deepseek-ai/DeepSeek-R1-Distill-Qwen-7B \
  --local-dir DeepSeek-R1-Distill-Qwen-7B

### llamafactory 安装

git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"

### 训练模型

CUDA_VISIBLE_DEVICES=0,1,3 llamafactory-cli train \
    --stage sft \
    --do_train True \
    --model_name_or_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
    --preprocessing_num_workers 16 \
    --finetuning_type lora \
    --template deepseek3 \
    --flash_attn auto \
    --dataset_dir data \
    --dataset distill_r1_110k \
    --cutoff_len 2000 \
    --learning_rate 5e-05 \
    --num_train_epochs 1.0 \
    --max_samples 100 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 5 \
    --save_steps 100 \
    --warmup_steps 0 \
    --packing False \
    --report_to none \
    --output_dir saves/DeepSeek-R1-7B-Distill/lora/train_2025-03-05-23-46-16 \
    --bf16 True \
    --plot_loss True \
    --trust_remote_code True \
    --ddp_timeout 180000000 \
    --include_num_input_tokens_seen True \
    --optim adamw_torch \
    --lora_rank 8 \
    --lora_alpha 16 \
    --lora_dropout 0 \
    --lora_target all


# 【大模型微调】使用 LLaMA-Factory 微调 LLaMA3

🎥 视频教程
- [YouTube](https://youtu.be/Hpc4QQQuLWM)
- [Bilibili](https://www.bilibili.com/video/BV1uw4m1S7Cd/?vd_source=2acabf9b10c0b70274da02f31cf31368)

## 1. 实验环境

### ⚙️ 1.1 机器

1. **Mac Mini M2**
2. **Ubuntu**
   - PyTorch 2.1.0
   - Python 3.10 (Ubuntu 22.04)
   - Cuda 12.1
   - RTX 4090 (24GB) * 1
   - CPU: 12 vCPU Intel(R) Xeon(R) Platinum 8352V CPU @ 2.10GHz

### 🦄 1.2 基座模型

基于中文数据训练过的 LLaMA3 8B 模型：  
[shenzhi-wang/Llama3-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat)

（可选）配置 hf 国内镜像站：
```bash
pip install -U huggingface_hub
pip install huggingface-cli

export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download --resume-download shenzhi-wang/Llama3-8B-Chinese-Chat --local-dir /root/autodl-tmp/models/Llama3-8B-Chinese-Chat1
```

## 2. LLaMA-Factory 框架

### ⚙️ 2.1 安装

```shell
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .
```

### 📂 2.2 准备训练数据

训练数据：
- [fintech.json](https://github.com/echonoshy/cgft-llm/blob/master/llama-factory/data/fintech.json)
- [identity.json](https://github.com/echonoshy/cgft-llm/blob/master/llama-factory/data/identity.json)

将训练数据放在 LLaMA-Factory/data/fintech.json  
并且修改数据注册文件：LLaMA-Factory/data/dataset_info.json

```json
"fintech": {
  "file_name": "fintech.json",
  "columns": {
    "prompt": "instruction",
    "query": "input",
    "response": "output",
    "history": "history"
  }
}
```

### 🌐 2.3 启动 Web UI

```shell
cd LLaMA-Factory
llamafactory-cli webui
```

### 🔧 2.4 微调模型

1. **使用 Web UI 训练**

2. **使用命令行执行**
   > 配置文件位于：[cust/train_llama3_lora_sft.yaml](https://github.com/echonoshy/cgft-llm/tree/master/llama-factory/cust)

构建 cust/train_llama3_lora_sft.yaml
```yaml
cutoff_len: 1024
dataset: fintech,identity
dataset_dir: data
do_train: true
finetuning_type: lora
flash_attn: auto
fp16: true
gradient_accumulation_steps: 8
learning_rate: 0.0002
logging_steps: 5
lora_alpha: 16
lora_dropout: 0
lora_rank: 8
lora_target: q_proj,v_proj
lr_scheduler_type: cosine
max_grad_norm: 1.0
max_samples: 1000
model_name_or_path: /root/autodl-tmp/models/Llama3-8B-Chinese-Chat
num_train_epochs: 10.0
optim: adamw_torch
output_dir: saves/LLaMA3-8B-Chinese-Chat/lora/train_2024-05-25-20-27-47
packing: false
per_device_train_batch_size: 2
plot_loss: true
preprocessing_num_workers: 16
report_to: none
save_steps: 100
stage: sft
template: llama3
use_unsloth: true
warmup_steps: 0
```

命令行执行：
```shell
llamafactory-cli train cust/train_llama3_lora_sft.yaml
```

### 💬 2.5 对话

1. **使用 Web UI 界面进行对话**
    ```shell
    llamafactory-cli webchat cust/train_llama3_lora_sft.yaml
    ```

2. **使用终端进行对话**
    ```shell
    llamafactory-cli chat cust/train_llama3_lora_sft.yaml
    ```

3. **使用 OpenAI API 风格进行对话**
    ```shell
    # 指定多卡和端口
    CUDA_VISIBLE_DEVICES=0,1 API_PORT=8000 
    llamafactory-cli api cust/train_llama3_lora_sft.yaml
    ```

### 🛠️ 2.6 模型合并

将 base model 与训练好的 LoRA Adapter 合并成一个新的模型。  
⚠️ 不要使用量化后的模型或 `quantization_bit` 参数来合并 LoRA 适配器。
```shell
llamafactory-cli export cust/merge_llama3_lora_sft.yaml
```

> 使用合并后的模型进行预测，就不需要再加载 LoRA 适配器。

### 🔢 2.7 模型量化

模型量化（Model Quantization）是一种将模型的参数和计算从高精度（通常是 32 位浮点数，FP32）转换为低精度（如 16 位浮点数，FP16，或者 8 位整数，INT8）的过程。
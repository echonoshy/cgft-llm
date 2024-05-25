
## 1. 实验环境
### 设备
1. Mac Mini M2
2. Ubuntu
	- PyTorch  2.1.0
	- Python  3.10(ubuntu22.04)
	- Cuda  12.1
	- RTX 4090(24GB) * 1
	- CPU12 vCPU Intel(R) Xeon(R) Platinum 8352V CPU @ 2.10GHz

### 基座模型
[shenzhi-wang/Llama3-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat)

配置hf国内镜像站：
```bash
pip install -U huggingface_hub
pip install hugginface-cli

export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download --resume-download shenzhi-wang/Llama3-8B-Chinese-Chat --local-dir /root/autodl-tmp/models/Llama3-8B-Chinese-Chat1
```

## 2. LLaMA-Factory 框架训练

### 1. 安装
```shell
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .  

```

### 2. 准备训练数据
train data: https://github.com/echonoshy/cgft-llm/blob/master/data/fintech.json

将训练数据放在data/fintech.json
修改： data/dataset_info.json

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

### 3. 启动Web UI
```shell
cd LLaMA-Factory
llamafactory-cli webui
```

### 4. 微调模型
1. 使用webui训练
![[Pasted image 20240525203212.png]]

2. 使用命令行执行

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

### 5. 对话

1. 使用web UI 界面进行对话
```
llamafactory-cli webchat cust/train_llama3_lora_sft.yaml
```

2. 使用终端进行对话
```shell
llamafactory-cli chat cust/train_llama3_lora_sft.yaml
```

3. 使用OpenAI API风格进行对话
```shell
# 指定多卡和端口
CUDA_VISIBLE_DEVICES=0,1 API_PORT=8000 
llamafactory-cli api cust/train_llama3_lora_sft.yaml
```

### 6.模型合并
⚠️ 不要使用量化后的模型或 `quantization_bit` 参数来合并 LoRA 适配器。
```shell
llamafactory-cli export cust/merge_llama3_lora_sft.yaml
```

使用合并后的模型进行预测，就不需要在听见Lora适配器。

### 7. 模型量化
 模型量化（Model Quantization）是一种将模型的参数和计算从高精度（通常是32位浮点数，FP32）转换为低精度（如16位浮点数，FP16，或者8位整数，INT8）的过程。
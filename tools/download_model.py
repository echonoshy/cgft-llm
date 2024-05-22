# 从huggingface 下载模型到指定路径
from transformers import AutoTokenizer, AutoModelForCausalLM


# 使用示例
model_id = "shenzhi-wang/Llama3-8B-Chinese-Chat"
cache_dir = "/root/autodl-tmp/models/"



# 下载并加载 tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    cache_dir=cache_dir,
    force_download=True  # 强制重新下载
)

# 下载并加载模型
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    cache_dir=cache_dir,
    force_download=True  # 强制重新下载
)
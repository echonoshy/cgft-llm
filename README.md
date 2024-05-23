# 金融大模型分享

## 模型Finetune
1. 下载经过中文微调过的llama3  
https://huggingface.co/models?sort=trending&search=llama3+chinese
![alt text](images/image.png)

替代品 **modelscope**： https://modelscope.cn/search?search=llama3

## 模型量化


## 模型部署
- 使用ollama部署服务

## RAG



## autodl环境设置
1. 使用huggingface镜像站下载
https://hf-mirror.com/

huggingface-cli 是 Hugging Face 官方提供的命令行工具，自带完善的下载功能。

1. 安装依赖
pip install -U huggingface_hub
Copy
2. 设置环境变量
Linux
export HF_ENDPOINT=https://hf-mirror.com

建议将上面这一行写入 ~/.bashrc。
3.1 下载模型
huggingface-cli download --resume-download gpt2 --local-dir gpt2

3.2 下载数据集
huggingface-cli download --repo-type dataset --resume-download wikitext --local-dir wikitext

可以添加 --local-dir-use-symlinks False 参数禁用文件软链接，这样下载路径下所见即所得，详细解释请见上面提到的教程。


3. 修改HF下载模型位置（可选）  
`export HF_HOME=/root/autodl-tmp/cache/`


GGUF（GPT-Generated Unified Format）是一种二进制文件格式，专门用于存储和加载大规模语言模型（LLMs）。这种格式的设计目标是实现快速加载和保存，以提高推理过程的效率。GGUF格式由Georgi Gerganov开发，他也是流行的C/C++推理框架llama.cpp的作者。

https://github.com/ggerganov/ggml/blob/master/docs/gguf.md


## Ollama

# 激活代理
`source /etc/network_turbo`



下载ollama linux:
`curl -fsSL https://github.com/ollama/ollama/releases/download/v0.1.38/ollama-linux-amd64 -o /root/autodl-tmp/apps/ollama-linux-amd64`

或者：
`wget -O /root/autodl-tmp/apps/ollama-linux-amd64 https://github.com/ollama/ollama/releases/download/v0.1.38/ollama-linux-amd64`


挂在软链接到目录：
`sudo ln -s /root/autodl-tmp/apps/ollama-linux-amd64 /usr/local/bin/ollama`
chmod +x /root/autodl-tmp/apps/ollama-linux-amd64

补充： 

- **`/bin`**：基本命令，必须在系统引导时和单用户模式下可用。ls, rm
- **`/usr/bin`**：标准用户命令，通常由系统包管理器安装，依赖于 `/usr` 文件系统。 sed, grep
- **`/usr/local/bin`**：本地安装的软件和脚本，不依赖于系统包管理器。


启动服务：
ollama server 
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit --local-dir /root/autodl-tmo/models/Llama3-8B-Chinese-Chat-GGUF
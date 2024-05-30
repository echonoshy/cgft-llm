
export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-4bit --local-dir /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF-4bit


https://github.com/open-webui/open-webui


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
huggingface-cli download shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit --local-dir /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF




## 1. 模型量化

将模型的权重和激活函数从高精度表示（如32位浮点数）转换为低精度表示（如16位浮点数或更低），从而减少模型的内存占用和计算量。


### 1. 安装
```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

```

补充：
**CMake** 是一个跨平台的构建系统生成工具。它的主要作用是通过配置文件（通常是 `CMakeLists.txt`）生成适合于目标平台的构建脚本或文件

**Make** 是一个构建自动化工具。它通过读取 Makefile 来执行编译和构建过程。g++/ gcc


### 编译
1. cpu
```
cmake -B build_cpu
cmake --build build_cpu --config Release
```

cuda
```
cmake -B build_cuda -DLLAMA_CUDA=ON
cmake --build build_cuda --config Release -j 12
```


##  准备模型文件

```
export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit --local-dir /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF
```



## 部署模型


```shell


./main -m /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf -n -1 -ngl 1 -t 12 --color -r "User:" --in-prefix " " -i -p \
'User: Hi
AI: Hello. I am an AI chatbot. Would you like to talk?
User: Sure!
AI: What would you like to talk about?
User:'







```


参数介绍：
https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md



### 部署服务

```

```


./quantize --allow-requantize /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q4_1-v1.gguf Q4_1


格式转换
python convert-hf-to-gguf.py /root/autodl-tmp/models/Llama3-8B-Chinese-Chat --outfile /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v1.gguf --outtype q8_0



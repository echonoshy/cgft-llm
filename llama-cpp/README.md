
# 【大模型量化】使用llama.cpp进行量化和部署

🎥 视频教程
- [YouTube](https://youtu.be/2MYsfe0pc9A)
- [Bilibili](https://www.bilibili.com/video/BV1et421N7TK/)

## 📝 1. 准备模型文件
- [shenzhi-wang/Llama3-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat)
- [shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit)

```bash
export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit --local-dir /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF
```

## 🔧 2. 安装
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```

## 🛠️ 3. 编译

补充：  
**CMake** 是一个跨平台的构建系统生成工具。它的主要作用是通过配置文件（通常是 `CMakeLists.txt`）生成适合于目标平台的构建脚本或文件

**Make** 是一个构建自动化工具。它通过读取 Makefile 来执行编译和构建过程。

**g++/clang/MinGW** 是负责具体编译的编译器。

**总结：**
- CMake 生成 Makefile。
- Make 读取 Makefile 并调用 g++ 进行编译和链接。
- g++ 是实际执行编译和链接的编译器。

### 🖥️ CPU 版本
```bash
cmake -B build_cpu
cmake --build build_cpu --config Release
```

### 🖥️ CUDA 版本
```bash
cmake -B build_cuda -DLLAMA_CUDA=ON
cmake --build build_cuda --config Release -j 12
```

## 🚀 4. 具体使用

### 🧩 4.1 主功能 main 
```bash
cd /root/code/llama.cpp/build_cuda/bin/

./main -m /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf \
    -n -1 \
    -ngl 256 \
    -t 12 \
    --color \
    -r "User:" \
    --in-prefix " " \
    -i \
    -p \
'User: 你好
AI: 你好啊，我是光屿，要聊聊吗?
User: 好啊!
AI: 你想聊聊什么话题呢？
User:'
```

[main 参数介绍](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

### 🌐 4.2 部署服务 server
```bash
cd ~/code/llama.cpp/build_cuda/bin

./server \
    -m /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf \
    --host "127.0.0.1" \
    --port 8080 \
    -c 2048 \
    -ngl 128 \
    --api-key "echo in the moon"
```

### 🔧 4.3 量化

混合精度量化：
1. fp16 -> int8 
2. fp16 -> fp16

🤔 思考：如果采样混合精度量化时，有的层是 fp16，有的层是 int8，计算时是怎样的呢？

1. 将 gguf 格式进行（再）量化
```bash
cd ~/code/llama.cpp/build_cuda/bin
./quantize --allow-requantize /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q4_1-v1.gguf Q4_1
```

2. 将 safetensors 格式转成 gguf
```bash
python convert-hf-to-gguf.py /root/autodl-tmp/models/Llama3-8B-Chinese-Chat --outfile /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF/Llama3-8B-Chinese-Chat-q8_0-v1.gguf --outtype q8_0
```

扩展阅读：  
[https://github.com/ggerganov/llama.cpp/pull/1684](https://github.com/ggerganov/llama.cpp/pull/1684)

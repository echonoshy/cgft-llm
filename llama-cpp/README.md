# 【大模型量化】使用llama.cpp进行量化和部署


## Llama.cpp

### 1. 安装
```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```


### 2. 编译

补充：  
**CMake** 是一个跨平台的构建系统生成工具。它的主要作用是通过配置文件（通常是 `CMakeLists.txt`）生成适合于目标平台的构建脚本或文件

**Make** 是一个构建自动化工具。它通过读取 Makefile 来执行编译和构建过程。g++/ gcc

**g++/clang/MinGW** 是负责具体编译的编译器。

**总结：**
    CMake 生成 Makefile。
    Make 读取 Makefile 并调用 g++ 进行编译和链接。
    g++ 是实际执行编译和链接的编译器。

cpu
```
cmake -B build_cpu
cmake --build build_cpu --config Release
```

cuda
```
cmake -B build_cuda -DLLAMA_CUDA=ON
cmake --build build_cuda --config Release -j 12
```


##  3.准备模型文件
- [shenzhi-wang/Llama3-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat)

- [shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit)

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



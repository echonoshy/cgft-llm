# 大模型快速部署工具 Ollama 介绍

Ollama 是一个轻量级的大语言模型部署和运行工具，支持多种开源模型的快速部署和使用。

## 🛠️ 安装 Ollama

### Mac 和 Windows 安装
Mac 和 Windows 具有成熟的一键安装工具，可直接从[官网](https://ollama.com)下载安装包。

### 🐧 在 Linux 上手动安装
尽管官方提供了一键安装脚本 `curl -fsSL https://ollama.com/install.sh | sh`，但在内网环境或特殊配置下，可能需要手动安装。

#### 1. 启动网络代理（如需要）
```bash
source /etc/network_turbo
```

#### 2. 下载安装包
```bash
# 方法1：手动从 GitHub releases 页面下载
# https://github.com/ollama/ollama/releases

# 方法2：使用命令行下载（注意替换为最新版本号）
curl -fsSL https://github.com/ollama/ollama/releases/download/v0.1.38/ollama-linux-amd64 -o /root/autodl-tmp/apps/ollama-linux-amd64

# 或者使用 wget
wget -O /root/autodl-tmp/apps/ollama-linux-amd64 https://github.com/ollama/ollama/releases/download/v0.1.38/ollama-linux-amd64
```

#### 3. 配置可执行权限并创建软链接
```bash
chmod +x /root/autodl-tmp/apps/ollama-linux-amd64
sudo ln -s /root/autodl-tmp/apps/ollama-linux-amd64 /usr/local/bin/ollama
```

> **补充说明**：Linux 二进制文件安装位置
> - **/bin**：基本命令，系统引导和单用户模式下可用（如 ls, rm）
> - **/usr/bin**：标准用户命令，通常由包管理器安装（如 sed, grep）
> - **/usr/local/bin**：本地安装的软件和脚本，不依赖系统包管理器

#### 4. 启动 Ollama 服务
```bash
ollama serve
```

## 💻 使用 Ollama

### 基本命令
```bash
ollama run llama3   # 拉取模型并开始对话
ollama list         # 显示已下载的模型列表
ollama rm llama3    # 删除指定模型
ollama pull llama3  # 仅下载模型，不开始对话
```

可用的模型比[官方库](https://ollama.com/library)列出的更多，建议查看 Hugging Face 上相应模型的说明，确认是否被 Ollama 支持。

### 🔌 REST API 调用方式

更多 API 详情请参考[官方 API 文档](https://github.com/ollama/ollama/blob/main/docs/api.md)。

#### 流式调用（逐 token 返回）
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Why is the sky blue?"
}'
```

#### 非流式调用（一次性返回完整回答）
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

#### 多轮对话（保持上下文）
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    },
    {
      "role": "assistant",
      "content": "due to rayleigh scattering."
    },
    {
      "role": "user",
      "content": "how is that different than mie scattering?"
    }
  ],
  "stream": false
}'
```

## 📂 加载本地模型

Ollama 支持 GGUF 格式模型。如果您的模型是其他格式，需要先使用 llama.cpp 转换为 GGUF。
**注意**：并非所有 GGUF 文件都与 Ollama 兼容。

### 1. 创建 Modelfile
```
FROM /path/to/your/model.gguf

# 设置温度参数（越高创造性越强，越低一致性越好）
PARAMETER temperature 1

# 设置系统提示
SYSTEM """
You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
"""
```

### 2. 加载模型
```bash
ollama create model_name -f ./Modelfile
# model_name: 在 Ollama 中显示的模型名称
# ./Modelfile: Modelfile 的路径（可以是相对或绝对路径）
```

### 3. 使用模型
```bash
ollama run model_name
```

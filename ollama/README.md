# Ollama

## 🕹️ 在linux上手动安装ollama

### 1. 启动autodl代理
```
source /etc/network_turbo
```

### 2. 手动下载安装包
下载ollama linux:  
```
curl -fsSL https://github.com/ollama/ollama/releases/download/v0.1.38/ollama-linux-amd64 -o /root/autodl-tmp/apps/ollama-linux-amd64

或者：
wget -O /root/autodl-tmp/apps/ollama-linux-amd64 https://github.com/ollama/ollama/releases/download/v0.1.38/ollama-linux-amd64
```

### 3. 挂在软连接
```
sudo ln -s /root/autodl-tmp/apps/ollama-linux-amd64 /usr/local/bin/ollama
chmod +x /root/autodl-tmp/apps/ollama-linux-amd64
```
补充： 

- **`/bin`**：基本命令，必须在系统引导时和单用户模式下可用。ls, rm
- **`/usr/bin`**：标准用户命令，通常由系统包管理器安装，依赖于 `/usr` 文件系统。 sed, grep
- **`/usr/local/bin`**：本地安装的软件和脚本，不依赖于系统包管理器。

### 4. 启动服务
启动服务：
```
ollama server 
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download shenzhi-wang/Llama3-8B-Chinese-Chat-GGUF-8bit --local-dir /root/autodl-tmp/models/Llama3-8B-Chinese-Chat-GGUF
```


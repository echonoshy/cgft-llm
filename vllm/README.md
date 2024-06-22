
# vllm部署工具及paged attention

🎥 视频教程
- [YouTube](https://youtu.be/cQWzKX9gM9Q)
- [Bilibili](https://www.bilibili.com/video/BV1R1421r7tk)

## 1. Vllm介绍
### 📝 1. 准备模型文件
- [THUDM/glm-4-9b-chat](https://huggingface.co/THUDM/glm-4-9b-chat)

使用huggingface 镜像站下载
```bash
export HF_ENDPOINT=https://hf-mirror.com

huggingface-cli download THUDM/glm-4-9b-chat --local-dir /root/autodl-tmp/models/glm-4-9b-chat
```

使用modelscope下载
```
pip install modelscope
modelscope download --model ZhipuAI/glm-4-9b-chat --local_dir /root/autodl-tmp/models/glm-4-9b-chat

# int4 量化模型
modelscope download --model qwen/Qwen2-1.5B --local_dir /root/autodl-tmp/models/qwen2-1.5b
```


### 2. 安装vllm
```
pip install vllm 
```


### 3. 使用vllm

3.1 推理 
```
python infer.py
```

3.2 部署服务
```
bash vllm_server.sh
```

3.3 调用服务
```
# 1.使用openai 风格的客户端调用
python openai_client.py

# 2. 使用gradio客户端
bash run_gradio_client.sh

```

### 4. Paged Attention介绍

[Paged Attention](https://blog.vllm.ai/2023/06/20/vllm.html)

1. 在 vLLM 中，LLM 服务的性能瓶颈在于内存。
2. KV Cache 的分块存储。
3. 共享内存对多输出序列的优化。



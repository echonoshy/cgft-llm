
# Graph RAG

## ollama本地部署graph rag服务

### 1. 环境配置

1.1 模型：
Qwen/Qwen2-7B-Instruct-GGUF qwen2-7b-instruct-q5_k_m.gguf

```
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download Qwen/Qwen2-7B-Instruct-GGUF qwen2-7b-instruct-q5_k_m.gguf --local-dir /root/autodl-tmp/models/
```

1.2 构建ollama model
```
ollama create qwen2-7b-instruct-q5_k_m -f /root/code/cgft-llm/graph-rag/src/Modelfile
```

1.3 修改emb接口
```bash
pip install graphrag

sudo find / -name openai_embeddings_llm.py
替换openai_embeddings_llm.py
```

测试接口
```
curl http://localhost:11434/api/embeddings -d '{
  "model": "qwen2-7b-instruct-q5_k_m",
  "prompt": "你今天去哪玩？"
}'
```


### 2. 初始化服务

```
mkdir -p graph-rag 
cd graph-rag

python3 -m graphrag.index --root ./
```

### 3. 构造KG

```
python3 -m graphrag.index --root ./
```

### 4. 推理
```
python3 -m graphrag.query --root ./ --method local "霸王茶姬香港店什么时候开业？"
python3 -m graphrag.query --root ./ --method global "Who is Fahd Mirza?"

```





# Graph RAG

## ollama本地部署graph rag服务

### 1. 环境配置

1.1 模型：
Qwen/Qwen2-7B-Instruct-GGUF qwen2-7b-instruct-q5_k_m.gguf

```
# 通过huggingface镜像站下载
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download Qwen/Qwen2-7B-Instruct-GGUF qwen2-7b-instruct-q5_k_m.gguf --local-dir /root/autodl-tmp/models/
```

1.2 构建ollama model

```
# 直接使用ollama pull的模型上下文长度有限，容易报错。推荐通过Modelfile方式手动构建模型，并指定一个较长的上下文。

ollama create qwen2-7b-instruct-q5_k_m -f /root/code/cgft-llm/graph-rag/src/Modelfile
```

1.3 修改emb接口

```bash
pip install graphrag
pip install ollama

sudo find / -name openai_embeddings_llm.py
使用src文件夹中的openai_embeddings_llm.py替换graphrag包中的同名文件

sudo find / -name embeddings.py
使用src文件夹中的embeddings.py替换graphrag包中的同名文件
⚠️ 如果你不是使用该模型（qwen2-7b-instruct-q5_k_m），请修改src替换文件中对应的模型名！！！
```

测试emb接口是否正常

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

python -m graphrag.index --init --root ./
```

### 3. 构造KG

```
python -m graphrag.index --root ./
```

### 4. 推理

```
python -m graphrag.query --root ./ --method local "霸王茶姬香港店什么时候开业？"
python -m graphrag.query --root ./ --method global "霸王茶姬香港店什么时候开业"

```

## Graph RAG 对比 Basic RAG

参考：https://www.bilibili.com/video/BV17i421h7wL/?spm_id_from=333.337.search-card.all.click&vd_source=2acabf9b10c0b70274da02f31cf31368

> 传统上，RAG（Retrieval-Augmented Answer Generation）方法在处理具体问题时表现良好，能够直接在知识库中检索出包含答案的段落，并进行融合生成回答。然而，对于宏观问题，如团队成就调查，RAG的效率和准确性则较差。这些问题要求获取散落在不同文档中的信息，并整合为连贯的答案。 GraphRAG通过构建知识图谱，将企业知识库中的相关信息进行分类和关联，形成层次结构。这种结构使得回答问题时，可以依据信息的相关性和层次性快速定位答案。同时，GraphRAG还引入了社区挖掘算法，进一步优化信息关联和聚合的过程。 尽管GraphRAG具有显著的潜力，但其实际应用仍面临挑战。首先是知识图谱的构建，这一过程需要大量的人工干预以去除噪声和进行校正。其次是计算资源的消耗，特别是在处理大型知识图谱时，计算复杂度较高。最后，新数据的加入需要频繁更新知识图谱，这可能要求从零开始构建整个图谱，带来额外的计算负担。

1. 成本
2. 应用场景
3. 应用能力
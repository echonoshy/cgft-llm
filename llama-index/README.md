# llama index 实现RAG

## 📷 朴素RAG思想
“ra + g" 

![Basic RAG](./assets/basic_rag.png)


## 🧹 RAG的Pipeline

### 1. Loading
从不同的来源中获取数据。  (Doc, PDF, API)
https://llamahub.ai/?tab=readers

### 2. Embedding 
将加载的Document切分成node（小块的数据），再使用模型进行vector embedding(向量化)

### 3. Storing
为了避免重复对数据进行向量化，将embedding存储在向量数据库中。

### 4. Indexing
将“问题”也进行embedding, 从向量库中检索出最相近的“知识”

### 5. Querying
使用增强后的数据（问题 + 检索到的信息）一同输入模型，获取答案。



## 🖌️ 代码样例

### 1. 对多个txt文本的检索问答
```
python llama-index/index-doc.py
```

### 2. 对复杂pdf数据源的问答
```
python llama-index/index-pdf.py
```

### 3. 拆解query过程
```
python llama-index/query.py
```
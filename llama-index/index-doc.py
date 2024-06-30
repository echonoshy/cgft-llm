from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding


# 加载数据
documents = SimpleDirectoryReader("llama-index/docs").load_data()

# Emb
Settings.embed_model = OllamaEmbedding(model_name="wangshenzhi/llama3-8b-chinese-chat-ollama-q8")  

# Post processing
Settings.llm = Ollama(model="wangshenzhi/llama3-8b-chinese-chat-ollama-q8", request_timeout=360)  


index = VectorStoreIndex.from_documents(
    documents
)

query_engine = index.as_query_engine()


# 执行查询并获取响应
response = query_engine.query("霸王茶姬香港店什么时候开业？店长薪酬多少？")
print(response)  
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, get_response_synthesizer, Settings
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding



# Emb
Settings.embed_model = OllamaEmbedding(model_name="wangshenzhi/llama3-8b-chinese-chat-ollama-q8")  

# Post processing
Settings.llm = Ollama(model="wangshenzhi/llama3-8b-chinese-chat-ollama-q8", request_timeout=360)  


# build index
documents = SimpleDirectoryReader("llama-index/docs").load_data()
index = VectorStoreIndex.from_documents(documents)



# configure retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=2,
)

# configure response synthesizer
response_synthesizer = get_response_synthesizer()

# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,    
)

# query
response = query_engine.query("霸王茶姬香港店什么时候开业？店长薪酬多少？")
print(response)

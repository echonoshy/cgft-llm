
# ref:
# https://llamahub.ai/l/readers/llama-index-readers-file?from=

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.readers.file import PDFReader


# load pdf
parser = PDFReader()
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
   "llama-index/pdf", file_extractor=file_extractor 
).load_data()
    


# emb 
Settings.embed_model = OllamaEmbedding(model_name="wangshenzhi/llama3-8b-chinese-chat-ollama-q8")  

# llm
Settings.llm = Ollama(model="wangshenzhi/llama3-8b-chinese-chat-ollama-q8", request_timeout=360)  


if not os.path.exists("llama-index/db/pdf-db"):
    index = VectorStoreIndex.from_documents(
        documents
    )
    index.storage_context.persist(persist_dir="llama-index/db/pdf-db")
    
else:
    storage_context = StorageContext.from_defaults(persist_dir="llama-index/db/pdf-db")
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()

# 执行查询并获取响应
response = query_engine.query("如果我想获得澳洲500签证， TOEFL最少要考多少分？")
print(response)  
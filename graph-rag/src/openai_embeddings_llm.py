# Modify:
# /root/miniconda3/lib/python3.10/site-packages/graphrag/llm/openai/openai_embeddings_llm.py


from typing_extensions import Unpack
from graphrag.llm.base import BaseLLM
from graphrag.llm.types import (
    EmbeddingInput,
    EmbeddingOutput,
    LLMInput,
)
from .openai_configuration import OpenAIConfiguration
from .types import OpenAIClientTypes
import ollama

class OpenAIEmbeddingsLLM(BaseLLM[EmbeddingInput, EmbeddingOutput]):
    _client: OpenAIClientTypes
    _configuration: OpenAIConfiguration

    def __init__(self, client: OpenAIClientTypes, configuration: OpenAIConfiguration):
        self._client = client
        self._configuration = configuration

    async def _execute_llm(
        self, input: EmbeddingInput, **kwargs: Unpack[LLMInput]
    ) -> EmbeddingOutput | None:
        args = {
            "model": self._configuration.model,
            **(kwargs.get("model_parameters") or {}),
        }
        embedding_list = []
        for inp in input:
            embedding = ollama.embeddings(model="qwen2-7b-instruct-q5_k_m", prompt=inp)
            embedding_list.append(embedding["embedding"])
        return embedding_list
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.messages import HumanMessage, SystemMessage



model = ChatOpenAI(
    base_url="http://localhost:11434/v1/chat/completions",
    api_key="EMPTY",
    model="wangshenzhi/llama3-8b-chinese-chat-ollama-q8",
)




messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)
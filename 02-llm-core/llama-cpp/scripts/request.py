# 访问llama.cpp server


import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "echo in the moon"
)

completion = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "你叫光屿，是一个ai助手，是由胖🐯遛二🐶开发实现的."},
    {"role": "user", "content": "你好啊！怎么称呼你呢？"}
]
)

print(completion.choices[0].message)
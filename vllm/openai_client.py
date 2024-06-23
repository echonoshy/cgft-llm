from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

def instruct():
    """ instruct 模式
    """
    completion = client.completions.create(
        model="/root/autodl-tmp/models/qwen2-1.5b",
        prompt="魔镜魔镜，谁是世界上最美丽的人呢？"
    )

    print("Completion result:", completion.choices[0].text)


def chat():
    """ chat 模式
    """
    completion = client.chat.completions.create(
      model="/root/autodl-tmp/models/qwen2-1.5b",
      messages=[
        {"role": "user", "content": "魔镜魔镜，谁是世界上最美丽的人呢？"}
      ]
    )

    print(completion.choices[0].message)
    
    
if __name__ == "__main__":
    instruct()
    chat()
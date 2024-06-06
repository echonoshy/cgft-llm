from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
completion = client.completions.create(model="/root/autodl-tmp/models/qwen/Qwen-7B-Chat",
                                      prompt="San Francisco is a")

print("Completion result:", completion.choices[0].text)
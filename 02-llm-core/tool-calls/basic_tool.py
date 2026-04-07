from openai import OpenAI
import json


def get_weather(location=""):
    weather_map = {
        "Hangzhou": "晴朗☀️，24度",
        "Shanghai": "多云☁️，14度",
        "Beijing": "小雨🌧️， 6度"
    }
    return weather_map.get(location, "暂无信息")


def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools
    )
    return response.choices[0].message


client = OpenAI(
    api_key="sk-xxxxxx",
    base_url="https://api.deepseek.com",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of an location, the user shoud supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]


# messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
messages = [{"role": "user", "content": "你好阿姨?"}]
message = send_messages(messages)
print(f"用户提问： {messages[0]['content']}")


if message.content:
    print(f"模型回复的内容是：{message.content}")

else:
    print("开始调用function calling 流程...")
    t = message.tool_calls[0]
    tool_name = t.function.name
    tool_params = json.loads(t.function.arguments)

    if tool_name == "get_weather":
        print(get_weather(tool_params["location"]))

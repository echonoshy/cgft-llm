# 使用Dify实现agent和LLM Workflow

## Agent及LLM Workflow

Agent和LLM Workflow都集成了LLM相关的技术，具备相当的智能，并且可以执行一些复杂功能。  
**区别**：Agent是通过多轮对话方式实现，LLM Workflow则是单轮的，给定输入得到输出。

## Dify

- 🌐 [官网](https://dify.ai)
- 📄 [文档](https://docs.dify.ai/zh-hans)
- 💻 [应用界面](https://cloud.dify.ai/apps)
- 🐙 [GitHub](https://github.com/langgenius/dify)

### 如何使用

#### 1. 基本配置
- 基础的LLM: 例如OpenAI API或者Ollama等本地部署服务
- 数据库(Knowledge)：用于RAG

#### 2. 构建方式
- 从空白模版构建
- 模版构建
- DSL配置文件构建（离线Fork别人工作流）

#### 3. 高级编辑模式
节点对应的文档请参考视频及文档：[Dify文档](https://docs.dify.ai/zh-hans/guides/workflow/node)

#### 4. 本地部署
推荐使用Docker部署，记得修改`.env`中的环境变量
```
cd dify
cd docker
cp .env.example .env
docker compose up -d
```

### 参考

1. 视频中提到的Web界面：
    1.1 复制整个文件夹：[GitHub链接](https://github.com/echonoshy/tingshu/tree/master/web)

    1.2 发布网站后，点击“嵌入网站”，将生成的内容粘贴到`index.html`文件中

    1.3 如果不想搞那么麻烦，也可以构建如下最简单的HTML。修改成对应的iframe
    ```
    <!DOCTYPE html>
    <html lang="zh-cn">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>嵌入iframe的示例</title>
    </head>
    <body>
        <h1>这是一个嵌入iframe的示例</h1>
        <iframe
            src="https://udify.app/chatbot/xxxxxxxxx"
            style="width: 100%; height: 100%; min-height: 700px"
            frameborder="0"
            allow="microphone">
        </iframe>
    </body>
    </html>
    ```

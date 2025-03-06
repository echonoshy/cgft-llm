# 使用 Dify 实现 Agent 和 LLM Workflow

## Agent 与 LLM Workflow 概念

Agent 和 LLM Workflow 都集成了 LLM 相关的技术，具备相当的智能，并且可以执行一些复杂功能。

**区别**：
- **Agent**：通过多轮对话方式实现功能
- **LLM Workflow**：单轮操作，给定输入直接得到输出

## Dify 平台介绍

Dify 是一个开源的 LLM 应用开发平台，提供了构建 Agent 和 Workflow 的能力。

- 🌐 [官网](https://dify.ai)
- 📄 [文档](https://docs.dify.ai/zh-hans)
- 💻 [应用界面](https://cloud.dify.ai/apps)
- 🐙 [GitHub](https://github.com/langgenius/dify)

## 使用指南

### 1. 基本配置

开始使用 Dify 需要配置：
- **基础 LLM**：可以是 OpenAI API 或者 Ollama 等本地部署服务
- **知识库(Knowledge)**：用于实现 RAG (检索增强生成)功能

### 2. 构建方式

Dify 提供多种构建应用的方式：
- 从空白模板构建
- 使用预设模板构建
- 通过 DSL 配置文件构建（可离线 Fork 他人的工作流）

### 3. 高级编辑模式

Dify 工作流支持多种节点类型，可实现复杂的逻辑和功能。详细节点说明请参考：
- [Dify 工作流节点文档](https://docs.dify.ai/zh-hans/guides/workflow/node)

### 4. 本地部署

推荐使用 Docker 进行本地部署：

```bash
cd dify
cd docker
cp .env.example .env
# 根据需要修改 .env 中的环境变量
docker compose up -d
```

## 应用集成参考

### Web 界面嵌入

1. 完整网站示例：
   - [GitHub 示例代码](https://github.com/echonoshy/tingshu/tree/master/web)

2. 嵌入流程：
   - 在 Dify 中创建应用后，点击"嵌入网站"
   - 将生成的嵌入代码粘贴到 `index.html` 文件中

3. 简易嵌入示例：

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dify 应用嵌入示例</title>
</head>
<body>
    <h1>Dify 应用嵌入</h1>
    <iframe
        src="https://udify.app/chatbot/xxxxxxxxx"
        style="width: 100%; height: 100%; min-height: 700px"
        frameborder="0"
        allow="microphone">
    </iframe>
</body>
</html>
```

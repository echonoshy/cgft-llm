# 大模型工具调用 (LLM Tool Calling)

本项目探索大型语言模型的工具调用能力，从基础实现到高级应用。

## 目录

- [大模型工具调用 (LLM Tool Calling)](#大模型工具调用-llm-tool-calling)
  - [目录](#目录)
  - [基础工具调用](#基础工具调用)
  - [关于 MCP](#关于-mcp)
  - [OpenAI Agent SDK](#openai-agent-sdk)
  - [Computer-use 和 Browser-use](#computer-use-和-browser-use)
  - [实践案例](#实践案例)
    - [实现一个极简的 Browser-use 功能](#实现一个极简的-browser-use-功能)

## 基础工具调用

基础的工具调用实现示例：

```python
python basic_tool.py
```

## 关于 MCP

Model Context Protocol (MCP) 是一种标准化大模型与外部环境交互的协议。

**相关资源:**
- [Model Context Protocol 官方文档](https://modelcontextprotocol.io/introduction)

## OpenAI Agent SDK

OpenAI 提供的官方代理开发工具包，便于构建基于大模型的智能代理。

**相关资源:**
- [OpenAI Agent SDK 官方文档](https://platform.openai.com/docs/guides/agents-sdk)

## Computer-use 和 Browser-use

探索大模型如何使用计算机和浏览器等工具进行交互。

**相关资源:**
- [browser-use GitHub 项目](https://github.com/browser-use/browser-use)

## 实践案例

### 实现一个极简的 Browser-use 功能

环境安装与配置:

```bash
pip install openai
pip install playwright

playwright install

# 运行示例
python github_trending_scraper.py
```
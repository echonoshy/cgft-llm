
# 🚀 Langfuse 快速入门教程

Langfuse 是一个强大的 LLM 应用观测平台，支持追踪（Trace）、生成（Generation）、评分、成本统计等功能。本教程演示如何在 Python 中初始化客户端、脱敏敏感数据、链式调用追踪、更新 trace/generation 信息等核心功能。

> ✅ 支持本地部署（如 `http://localhost:8300`）或云端 SaaS 版本  
> ✅ 支持自动/手动埋点、链式追踪、成本与 Token 统计  
> ✅ 支持敏感数据脱敏（可选）

---

## 📦 安装依赖

确保已安装 `langfuse` SDK：

```bash
pip install langfuse
```

---

## 🧩 完整示例代码

```python
from langfuse import Langfuse, observe
import os
import time
import uuid


# ========== 1. 可选：敏感数据脱敏函数 ==========
def masking_function(data: any, **kwargs) -> any:
    """
    脱敏函数：在发送到 Langfuse 之前对敏感数据进行处理
    示例：任何以 "SECRET_" 开头的字符串都会被替换为 "REDACTED"
    """
    if isinstance(data, str) and data.startswith("SECRET_"):
        return "REDACTED"
    return data


# ========== 2. 初始化 Langfuse 客户端 ==========
lf = Langfuse(
    secret_key="sk-lf-2939c17c-eceb-460c-ad39-39e9d2c110b8",
    public_key="pk-lf-caaeb59e-22c6-4979-b75c-57f832ada4c3",
    host="http://localhost:8300",  # 本地部署地址，如使用云服务请替换为 https://cloud.langfuse.com
    # mask=masking_function,  # 如果需要脱敏功能，取消注释启用
)

# 设置环境（可选）—— 在 Langfuse UI 中按环境过滤 trace
# os.environ["LANGFUSE_TRACING_ENVIRONMENT"] = "prod"


# ========== 3. 示例函数：链式调用（注释状态，可取消注释测试） ==========
# @observe
# def add_1(x: int) -> int:
#     time.sleep(0.1)
#     return x + 1
#
# @observe
# def add_2(x: int) -> int:
#     time.sleep(0.2)
#     return x + 2
#
# @observe
# def add(x: int) -> int:
#     y = add_1(x)
#     z = add_2(y)
#     return z


# ========== 4. 示例函数：更新 trace / generation ==========
@observe
def say_hi(name: str) -> str:
    """
    示例：在函数中更新 trace 和 generation 的信息
    - 设置用户 ID、会话 ID、元数据、标签等
    - 设置模型名称、Token 使用量、成本详情等
    """
    # 更新当前 trace 信息（顶层追踪）
    lf.update_current_trace(
        user_id="user_123",                  # 用户标识，用于分析用户行为
        # session_id="session_456",          # 会话标识（可选）
        # metadata={"custom_key": "custom_value"},  # 自定义元数据（可选）
        # tags=["tag1", "tag2"],             # 标签分类（可选）
    )

    # 更新当前 generation 信息（通常是 LLM 调用）
    lf.update_current_generation(
        model="gpt-4",                       # 模型名称
        usage_details={
            "prompt_tokens": 10,             # 输入 token 数
            "completion_tokens": 20,         # 输出 token 数
            "total_tokens": 30,              # 总 token 数
            "fake_tokens": 999,              # 自定义字段（非标准，但 Langfuse 支持）
            "input": 23000,                  # 自定义输入成本单位
            "output": 24000,                 # 自定义输出成本单位
            "total": 1110,                   # 自定义总成本单位
        },
        cost_details={
            "input": 1,                      # 输入成本（美元或其他单位）
            "cache_read_input_tokens": 2,    # 缓存读取的输入 token（Langfuse 新特性）
            "output": 3,                     # 输出成本
            "total": 6,                      # 总成本
        },
    )

    return f"{name} says hi!"


# ========== 5. 主程序入口 ==========
if __name__ == "__main__":
    # 生成唯一的 trace_id（32 位 hex 字符串）
    trace_id = uuid.uuid4().hex
    print(f"Generated Trace ID: {trace_id} (length: {len(trace_id)})")

    # 调用观测函数，并传入 trace_id 以关联整个调用链
    # add(3, langfuse_trace_id=trace_id)           # 链式调用示例（需取消上面注释）
    result = say_hi("Tencent", langfuse_trace_id=trace_id)
    print(f"Result: {result}")

    # 测试脱敏功能（如果启用了 masking_function）
    # say_hi("SECRET_ID_9527", langfuse_trace_id=trace_id)

    # 刷新并确保所有数据上报完成（推荐生产环境使用）
    lf.flush()
```

---

## 🛠️ 使用说明

### 1. 替换密钥和 Host
请将以下值替换为你自己的 Langfuse 实例配置：

```python
secret_key="YOUR_SECRET_KEY",
public_key="YOUR_PUBLIC_KEY",
host="YOUR_LANGFUSE_HOST",  # 如 https://cloud.langfuse.com 或 http://localhost:8300
```

> 🔐 生产环境中请通过环境变量管理密钥：
> ```bash
> export LANGFUSE_SECRET_KEY=sk-lf-xxx
> export LANGFUSE_PUBLIC_KEY=pk-lf-xxx
> export LANGFUSE_HOST=https://cloud.langfuse.com
> ```

然后在代码中初始化时无需传参：
```python
lf = langfuse.get_client()  # 自动从环境变量读取，全局单例
```

---

### 2. 启用脱敏功能

取消以下行注释以启用敏感数据脱敏：

```python
mask=masking_function,
```

你也可以自定义脱敏逻辑，例如屏蔽身份证、手机号、API Key 等。

---

### 3. 链式调用追踪

取消 `add`, `add_1`, `add_2` 函数的注释，即可看到嵌套调用在 Langfuse UI 中形成的调用树（Trace Tree）。

---

### 4. 查看结果

运行脚本后，访问你的 Langfuse 控制台（如 `http://localhost:8300`），搜索对应的 `trace_id`，即可查看：

- 调用层级结构
- 每个步骤耗时
- 用户/会话/标签信息
- Token 使用量 & 成本统计

---

## 📌 注意事项

- `@observe` 装饰器会自动创建 span，嵌套调用会形成父子关系。
- `lf.update_current_trace()` 和 `lf.update_current_generation()` 必须在 `@observe` 函数内部调用才有效。
- 所有数据默认异步上报，调用 `lf.flush()` 可强制同步刷新，确保程序退出前数据不丢失。
- 自定义字段（如 `fake_tokens`, `input`, `output`）会被 Langfuse 接收并展示，可用于内部统计。

---

## 📚 更多资源

- Langfuse 官网：https://langfuse.com
- Python SDK 文档：https://langfuse.com/docs/sdk/python

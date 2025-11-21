# Pytest 核心概念指南

## 1. 断言详解 (Assertions)

pytest 直接使用 Python 原生的 `assert` 关键字，不需要引入额外的断言库。

```python
# 1. 基本形式
assert condition

# 2. 带自定义错误信息
assert condition, "Error message if assertion fails"
```

> **注意**：断言主要用于开发和测试阶段，不要在生产代码的关键业务逻辑中仅依赖断言（因为 python -O 运行时会忽略断言）。

---

## 2. 发现规则 (Discovery Rules)

pytest 默认按照以下规则搜索测试：

### 文件名规则
- `test_*.py` (以 `test_` 开头的 Python 文件)
- `*_test.py` (以 `_test` 结尾的 Python 文件)

### 函数与类名规则
```python
def test_something():       # 以 test_ 开头的函数
    assert 1 + 1 == 2

class TestSomething:        # 以 Test 开头的类
    def test_method(self):  # 以 test_ 开头的方法
        assert True
```

### 运行方式
```bash
# 1. 自动搜索：在当前目录及其子目录中搜索
pytest

# 2. 指定目录
pytest tests/
pytest src/

# 3. 指定特定文件
pytest main.py

# 4. 运行特定测试函数 (文件::函数)
pytest tests/test_basic.py::test_addition
```

---

## 3. 测试函数 (Test Functions)

测试函数是 pytest 的最基本单元。

### 基本特征
- 函数名必须以 `test_` 开头。
- 通常不接受参数（除非使用 `fixture` 或 `parametrize`）。
- 使用 `assert` 语句进行断言。
- 通过返回值或异常来表示测试结果。

### 断言与异常处理

#### A. 普通断言 (期望成功)
验证代码逻辑是否符合预期。
```python
def test_basic():
    assert 1 == 1  # 如果条件为 False，测试失败
```

#### B. 异常断言 (期望抛出错误)
验证代码在错误输入下是否正确抛出了异常（使用 `pytest.raises`）。

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be 0")
    return a / b

def test_divide_zero():
    # 断言：执行 divide(1, 0) 时应该抛出 ValueError
    with pytest.raises(ValueError):
        divide(1, 0)
```

---



## 4. Fixture 夹具 (Fixtures)

Fixture 用于处理测试前置准备（Setup）和后置清理（Teardown），以及数据共享。

### 基本用法
```python
import pytest

@pytest.fixture
def sample_data():
    """返回测试数据"""
    print('>>> Setup')
    # yield 之前的代码相当于 Setup
    yield {"name": "Alice", "age": 30, "city": "New York"}
    # yield 之后的代码相当于 Teardown
    print('<<< Teardown')

def test_user_name(sample_data):
    # sample_data 作为参数传入，获取 yield 返回的值
    assert sample_data["name"] == "Alice"
```
> **提示**：要看到 fixture 中的 print 输出，运行时需要加 `-s` 参数：`pytest -s`

### Fixture 作用域 (Scope)
通过 `@pytest.fixture(scope="...")` 指定共享范围：

| 作用域 | 说明 | 典型应用场景 |
| :--- | :--- | :--- |
| **function** (默认) | 每个测试函数运行一次 | 独立的数据、清理数据库记录 |
| **class** | 每个测试类运行一次 | 测试类共享的配置 |
| **module** | 每个模块 (`.py`文件) 运行一次 | 模块级别的连接 |
| **session** | 整个测试会话只运行一次 | 全局配置、浏览器实例、数据库连接池 |

---

## 5. Mark 标记 (Marks)

使用 Mark 给测试分类，便于筛选运行。

### 定义标记
```python
import pytest

@pytest.mark.p1
def test_feature_a():
    assert True

@pytest.mark.slow
def test_network_op():
    pass

@pytest.mark.p1
@pytest.mark.slow
def test_complex():
    pass
```

### 运行指定标记
使用 `-m` 参数支持逻辑表达式：

```bash
# 运行标记为 p1 的测试
pytest -m "p1"

# 运行标记为 p1 或 slow 的测试
pytest -m "p1 or slow"

# 运行同时标记为 p1 和 slow 的测试
pytest -m "p1 and slow"

# 运行不包含 p1 标记的测试
pytest -m "not p1"
```

---

## 6. 参数化 (Parametrize)

使用 `@pytest.mark.parametrize` 实现数据驱动测试，用多组数据测试同一个逻辑。

```python
import pytest

# 定义参数名和参数值列表
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30),
])
def test_addition(x, y, expected):
    assert x + y == expected
```

---

## 7. 常用命令行参数

| 命令 | 作用 | 示例 |
| :--- | :--- | :--- |
| `pytest -v` | **Verbose**，显示详细输出 | 查看每个测试函数的执行结果 |
| `pytest -s` | **Standard Output**，捕获/显示标准输出 | 查看 print 语句的输出 |
| `pytest -m` | **Marker**，根据标记运行 | `pytest -m "smoke"` |
| `pytest -k` | **Keyword**，根据名称关键字运行 | `pytest -k "user or login"` |
| `pytest -n` | **Num processes**，多进程并行运行 | `pytest -n 4` (需要 `pytest-xdist` 插件) |

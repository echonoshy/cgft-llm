# ruff 教程

官方仓库： https://github.com/astral-sh/ruff

安装：`curl -LsSf https://astral.sh/ruff/install.sh | sh`

或者：
```bash
# With uv
uv tool install ruff          # 全局安装
uv add --dev ruff             # 项目内开发依赖

# With pip
pip install ruff
```

### 常用命令与功能

1) ruff check（静态检查）
```bash
ruff check .                          # 检查当前目录
ruff check --fix .                    # 自动修复可修复问题
ruff check --diff .                   # 仅显示将要修改的 diff
ruff check --watch .                  # 监听文件变更，实时检查
ruff check path/to/file.py            # 指定文件或目录
```
在代码中可用内联忽略（谨慎使用）：
```python
import pandas as pd  # noqa: F401
```

2) ruff format（代码格式化）
```bash
ruff format .               # 直接格式化
ruff format --check .       # 只检查是否需要格式化（CI 常用）
ruff format --diff .        # 展示格式化差异
```

3) ruff rule（查询规则说明）
```bash
ruff rule E501              # 查看某条规则详情
ruff rule --all             # 列出所有规则
```

4) ruff config（查看当前配置）
```bash
ruff config                 # 查看一级配置信息
ruff config lint            # 查看二级配置信息
```

5) ruff server（LSP 服务器，用于编辑器集成）
```
使用vscode 等工具的插件
```

6) 清理缓存

Ruff 没有 `ruff clean` 命令。若需清理缓存，可删除项目根目录下的 `.ruff_cache/`：
```bash
rm -rf .ruff_cache
```

---

### 装 VS Code 插件使用

- 安装 “Ruff” 扩展（由 Astral 发布）。
- 启用 “Format on Save” 可让 `ruff format` 在保存时生效。
- 扩展会自动使用 `ruff server` 提供诊断与快速修复。

---

### 如何配置 Ruff

Ruff 会从以下位置读取配置（优先级：命令行 > pyproject.toml > ruff.toml/.ruff.toml）：

- `pyproject.toml` 下的 `[tool.ruff]`、`[tool.ruff.lint]`、`[tool.ruff.format]`
- `ruff.toml` 或 `.ruff.toml`

最小示例（pyproject.toml）：
```toml
[tool.ruff]
line-length = 88
target-version = "py39"

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F"]
fixable = ["ALL"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

参考项目：
```bash
https://github.com/infiniflow/ragflow
```

# UV 教程

- 官方文档：https://docs.astral.sh/uv/

## 安装
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# 或
pip install uv
```

## 初始化项目
```bash
uv init
```

## 配置源
- 方法 1：环境变量
```bash
# 临时（当前 shell）
export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"

# 永久（追加到 .bashrc 或 .zshrc）
echo 'export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"' >> ~/.bashrc
```

- 方法 2：在 pyproject.toml
```toml
[tool.uv]
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

## Python 管理
```bash
uv python           # 查看帮助
uv python list      # 列出可用的 Python 版本
uv python install 3.13  # 安装指定版本
```

## 虚拟环境
```bash
uv venv                             # 创建虚拟环境（可从 pyproject.toml 指定 Python 版本）
source .venv/bin/activate           # 激活虚拟环境（POSIX）
```

## 项目依赖管理
```bash
uv add <package>       # 添加依赖
uv remove <package>    # 移除依赖

# 对比传统 pip 命令
uv pip install <package>
pip install <package>
```

## 工具管理
```bash
uv tool install <tool>     # 安装工具
uv tool uninstall <tool>   # 卸载工具
uv tool upgrade <tool>     # 升级工具
uv tool list               # 查看已安装工具
uv tool dir                # 工具存放目录
uv tool run <command>      # 运行工具（相当于 uvx）
```

## 运行程序
在激活虚拟环境的情况下，两者一致：
```bash
uv run main.py
python main.py
```

### 查看解释器
```bash
# 当前 shell 的解释器
which python
python -c "import sys; print(sys.executable, sys.version)"

# uv 使用的解释器（由 uv 选择/运行）
uv run -- python -c "import sys; print(sys.executable, sys.version)"
```

## 版本与更新
```bash
uv version        # 查看项目版本
uv self version   # 查看 uv 本身版本
uv self update    # 升级 uv
```

## 同步与锁文件
```bash
uv sync    # 按 pyproject.toml 构建依赖
uv lock    # 创建 uv.lock
uv export  # 导出依赖（不推荐）
```

## 缓存管理
```bash
uv cache dir     # 查看缓存目录
uv cache clean   # 清空全部缓存
uv cache prune   # 清除无用包
```




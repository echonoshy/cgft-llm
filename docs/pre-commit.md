

# 📘 Pre-commit

## 一、简介

* **参考文档**：

  * [Pre-commit 官方文档](https://pre-commit.com/)
  * [Git Hook 文档](https://git-scm.com/docs/githooks)

---

## 二、基础概念

* **Git Hook**：Git 提交前/后执行的脚本机制。
* **Pre-commit**：一个统一管理 Git Hook 的工具，自动执行格式化、检查等操作。
* **优势**：自动化、统一规范、减少低级错误。

---

## 三、快速上手

### 1. 安装

```bash
pip install pre-commit
```

### 2. 初始化

```bash
pre-commit install
```

### 3. 测试运行

```bash
pre-commit run --all-files
```

---

## 四、配置文件示例

📄 `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
```

> 🔗 更多示例：[参考配置文件（fastmcp 项目）](https://github.com/jlowin/fastmcp/blob/main/.pre-commit-config.yaml)

---

## 五、常用命令

```bash
pre-commit run --all-files   # 检查全部文件
pre-commit autoupdate        # 更新 hook 版本
pre-commit install           # 启用钩子
pre-commit uninstall         # 取消钩子
pre-commit clean             # 清除缓存

```

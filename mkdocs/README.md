# 使用mkdocs构建项目文档 

## 1. 本地化构建

1.1 环境安装

```
pip install mkdocs
```

1.2 初始化项目

```
mkdocs new .

mkdocs serve
```

1.3 配置主题
https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes

例如：material

```
pip install mkdocs-material
```

模版参考：

> https://github.com/echonoshy/Maozedong-xuanji




## 2. 远程服务托管

2.1 使用rtd远程托管

> https://readthedocs.org/

2.2 项目配置

- 关联github
- 配置webhook

readthedocs.yaml
```yaml
# Read the Docs configuration file for MkDocs projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.12"

mkdocs:
  configuration: mkdocs.yml

# Optionally declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
```
# 使用官方 python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到容器的 /app 目录
COPY . .

# 安装所需的 Python 库
RUN pip install requests

# 启动脚本
CMD ["python", "app.py"]

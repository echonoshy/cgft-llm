
### 1. 基本概念

- **Dockerfile**：一个文本文件，其中包含了一系列指令，Docker 引擎根据这些指令构建镜像。
- **镜像**：Dockerfile 构建后生成的可执行软件包，包含了运行应用所需的代码、库、环境变量等。
- **层**：Docker 镜像由多个层（Layer）构成，每一条指令都会创建一个新的层。层是不可变的，这使得 Docker 镜像更为高效和可重用。

### 2. 常用指令

以下是一些常用的 Dockerfile 指令：

| 指令           | 说明                                                      |
|----------------|-----------------------------------------------------------|
| `FROM`         | 指定基础镜像，Dockerfile 的第一行通常是此指令。            |
| `MAINTAINER`   | 指定维护者信息（不推荐使用，使用 LABEL 替代）。            |
| `LABEL`        | 添加元数据到镜像，例如作者、版本等。                        |
| `RUN`          | 在构建镜像时执行命令（例如安装软件包）。                    |
| `CMD`          | 指定容器启动时要执行的命令，可以被 `docker run` 命令覆盖。  |
| `ENTRYPOINT`   | 设置容器启动时的默认命令，不能被 `docker run` 轻易覆盖。   |
| `COPY`         | 将文件或目录从主机复制到镜像中。                            |
| `ADD`          | 类似于 COPY，但还支持 URL 和自动解压压缩文件。              |
| `ENV`          | 设置环境变量。                                            |
| `EXPOSE`       | 声明容器监听的端口，但并不会实际映射到主机。                |
| `VOLUME`       | 创建挂载点，用于持久化数据。                                |
| `WORKDIR`      | 设置工作目录，后续指令将在此目录下执行。                    |
| `ARG`          | 定义构建时可用的变量。                                    |
| `USER`         | 指定运行时的用户。                                        |
| `SHELL`        | 指定默认的 shell，用于运行后续指令。                        |

### 3. Dockerfile 示例


```Dockerfile
FROM python:3.10-slim 

LABEL maintainer="panhu"
LABEL version=1.0
LABEL desc="A docker bigv"

WORKDIR /app

ARG APP_VER=1.0
ENV APP_ENV=1.0

COPY . /app/
EXPOSE 5000

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD curl --fail http://localhost:5000/ || exit 1

RUN pip install flask


CMD ["python", "app.py"]

```

### 4. 构建镜像

使用 Dockerfile 构建镜像的命令：

```bash
docker build -t my-app .
```



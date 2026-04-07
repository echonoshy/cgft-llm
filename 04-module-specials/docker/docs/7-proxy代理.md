
### 1. 设置 Docker 引擎的代理（全局配置）
这种方法用于让所有 Docker 容器默认通过代理访问外部网络。

#### 步骤：
1. **创建或修改 Docker 引擎的配置文件：**

   对于 Linux 系统，Docker 的配置文件通常位于 `/etc/systemd/system/docker.service.d/`，或者 `/etc/docker/daemon.json`。
   
   首先，创建目录（如果不存在）：
   ```bash
   sudo mkdir -p /etc/systemd/system/docker.service.d
   ```

2. **创建或编辑 Docker 服务代理配置文件：**

   编辑 `/etc/systemd/system/docker.service.d/http-proxy.conf` 文件（如果没有该文件则创建），内容如下：
   ```ini
   [Service]
   Environment="HTTP_PROXY=http://host.docker.internal:proxy-port"
   Environment="HTTPS_PROXY=https://host.docker.internal:proxy-port"
   Environment="NO_PROXY=localhost,127.0.0.1"
   ```

   - `HTTP_PROXY` 和 `HTTPS_PROXY` 分别设置 HTTP 和 HTTPS 的代理地址。
   - `NO_PROXY` 则指定不需要通过代理访问的地址，比如本地地址。

3. **重新加载并重启 Docker 服务：**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ```

### 2. 针对单个 Docker 容器设置代理
如果不想全局配置 Docker 引擎的代理，而是希望为某个特定容器配置代理，可以在运行容器时使用环境变量设置。

#### 运行容器时指定代理：
在 `docker run` 命令中，通过 `-e` 参数传递代理环境变量：
```bash
docker run -e HTTP_PROXY=http://host.docker.internal:proxy-port \
           -e HTTPS_PROXY=https://host.docker.internal:proxy-port \
           -e NO_PROXY=localhost,127.0.0.1 \
           your-image

```

### 3. 配置 Dockerfile 中的代理
在构建 Docker 镜像时，也可以在 `Dockerfile` 中设置代理环境变量，确保在 `RUN` 指令执行时使用代理。

#### Dockerfile 示例：
```dockerfile
FROM ubuntu:20.04

# 设置代理环境变量
ENV HTTP_PROXY=http://host.docker.internal:proxy-port
ENV HTTPS_PROXY=https://host.docker.internal:proxy-port
ENV NO_PROXY=localhost,127.0.0.1

# 后续的指令会通过代理访问网络
RUN apt-get update && apt-get install -y curl
```

### 4. 配置 Docker Compose 的代理
如果使用 Docker Compose 管理多个容器，可以在 `docker-compose.yml` 文件中配置环境变量。

#### docker-compose.yml 示例：
```yaml
version: '3'
services:
  myservice:
    image: myimage
    environment:
      - HTTP_PROXY=http://host.docker.internal:proxy-port
      - HTTPS_PROXY=https://host.docker.internal:proxy-port
      - NO_PROXY=localhost,127.0.0.1
```

# 验证

```

docker run --rm -it nginx bash
curl www.google.com
```
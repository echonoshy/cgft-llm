
### 1. 容器生命周期管理
- **`docker run`**：启动一个新容器。例如：
  ```bash
  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
  ```
  常用选项：
  - `-d`：后台运行容器。
  - `-it`：以交互模式运行容器，并打开终端。
  - `--name`：为容器命名。
  - `-p`：端口映射，将主机的端口映射到容器。
  - `-v`：卷挂载，将主机目录映射到容器内的目录。

- **`docker start`**：启动一个已经停止的容器。例如：
  ```bash
  docker start <container_name|container_id>
  ```

- **`docker stop`**：停止运行的容器。例如：
  ```bash
  docker stop <container_name|container_id>
  ```

- **`docker restart`**：重启容器。例如：
  ```bash
  docker restart <container_name|container_id>
  ```

- **`docker kill`**：强制停止容器。例如：
  ```bash
  docker kill <container_name|container_id>
  ```

- **`docker rm`**：删除一个已停止的容器。例如：
  ```bash
  docker rm <container_name|container_id>
  ```

- **`docker exec`**：在正在运行的容器中执行命令。例如：
  ```bash
  docker exec -it <container_name|container_id> <command>
  ```

### 2. 查看容器状态
- **`docker ps`**：列出当前正在运行的容器。例如：
  ```bash
  docker ps
  ```
  常用选项：
  - `-a`：列出所有容器，包括已停止的容器。

- **`docker inspect`**：查看容器的详细信息。例如：
  ```bash
  docker inspect <container_name|container_id>
  ```

- **`docker logs`**：查看容器的日志输出。例如：
  ```bash
  docker logs <container_name|container_id>
  ```
  常用选项：
  - `-f`：实时查看日志。
  - `--tail`：只查看最近的若干行日志。

### 3. 容器资源管理
- **`docker top`**：查看容器中的进程。例如：
  ```bash
  docker top <container_name|container_id>
  ```

- **`docker stats`**：实时显示容器的资源使用情况（CPU、内存、网络等）。例如：
  ```bash
  docker stats
  ```

### 4. 容器文件系统管理
- **`docker cp`**：在容器和主机之间拷贝文件。例如：
  ```bash
  docker cp <container_name|container_id>:<container_path> <host_path>
  ```

- **`docker commit`**：将当前容器的更改提交为一个新镜像。例如：
  ```bash
  docker commit <container_name|container_id> <new_image_name>
  ```

### 5. 网络管理
- **`docker network ls`**：列出 Docker 网络。
- **`docker network create`**：创建新的 Docker 网络。
- **`docker network connect`**：将容器连接到某个网络。
- **`docker network disconnect`**：将容器从网络中断开。

### 6. 容器卷管理
- **`docker volume ls`**：列出所有卷。
- **`docker volume create`**：创建一个新卷。
- **`docker volume rm`**：删除卷。

### 7. 停止和删除所有容器（批量操作）
- **停止所有容器**：
  ```bash
  docker stop $(docker ps -q)
  ```
- **删除所有容器**：
  ```bash
  docker rm $(docker ps -a -q)
  ```

### 8. 其他
- **`docker attach`**：附加到运行中的容器终端。例如：
  ```bash
  docker attach <container_name|container_id>
  ```
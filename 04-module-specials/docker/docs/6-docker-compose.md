
### 1. 启动服务

```bash
docker-compose up
```
- **作用**：根据 `docker-compose.yml` 文件启动所有定义的服务。如果镜像不存在，它会自动构建或拉取所需的镜像。
- **常用选项**：
  - `-d`：后台运行容器（**detached mode**），不显示日志输出。
    ```bash
    docker-compose up -d
    ```
  - `--build`：强制重新构建服务，即使已经存在镜像。
    ```bash
    docker-compose up --build
    ```

### 2. 停止服务

```bash
docker-compose stop
```
- **作用**：停止正在运行的服务，但不删除容器。
- 停止后，容器的状态会保留，容器数据不会丢失。

### 3. 停止并删除所有服务

```bash
docker-compose down
```
- **作用**：停止并删除所有服务、网络和卷（除非显式定义了 `volumes` 持久化）。
- **常用选项**：
  - `--volumes`：同时删除与服务相关联的卷（慎用！可能会丢失持久化的数据）。
    ```bash
    docker-compose down --volumes
    ```
  - `--rmi`：删除与服务关联的镜像。
    ```bash
    docker-compose down --rmi all
    ```

### 4. 查看容器状态

```bash
docker-compose ps
```
- **作用**：查看当前 `docker-compose.yml` 定义的容器的运行状态，包括容器名、状态、端口映射等信息。

### 5. 重启服务

```bash
docker-compose restart
```
- **作用**：重新启动所有服务，或者可以通过指定服务名来重启某个服务。
- **示例**：
  ```bash
  docker-compose restart python-app
  ```

### 6. 构建服务

```bash
docker-compose build
```
- **作用**：根据 `docker-compose.yml` 文件中的定义重新构建服务镜像。
- **常用选项**：
  - `--no-cache`：在构建镜像时不使用缓存，强制构建新镜像。
    ```bash
    docker-compose build --no-cache
    ```

### 7. 查看服务日志

```bash
docker-compose logs
```
- **作用**：查看服务的日志输出，类似于使用 `docker logs` 查看单个容器的日志。
- **常用选项**：
  - `-f`：实时查看日志（类似 `tail -f`）。
    ```bash
    docker-compose logs -f
    ```
  - 指定特定服务的日志：
    ```bash
    docker-compose logs python-app
    ```

### 8. 运行单个命令

```bash
docker-compose run <service_name> <command>
```
- **作用**：在指定的服务中运行命令。与 `docker exec` 类似，但 `docker-compose run` 会启动一个新容器实例来运行命令，而不是在现有的容器中执行。
- **示例**：
  ```bash
  docker-compose run python-app python manage.py migrate
  ```

### 9. 进入容器

```bash
docker-compose exec <service_name> <command>
```
- **作用**：在运行的容器中执行命令（与 `docker exec` 类似）。
- **示例**：
  ```bash
  docker-compose exec python-app bash
  ```
  这将启动 `python-app` 服务的一个交互式 `bash` shell。

### 10. 查看容器使用的网络

```bash
docker-compose network ls
```
- **作用**：查看当前 `docker-compose` 管理的网络。

### 11. 扩展服务

```bash
docker-compose up --scale <service_name>=<num>
```
- **作用**：扩展某个服务的副本数量（多实例）。例如，你想扩展某个服务以便运行多个副本（通常用于负载均衡）。
- **示例**：
  ```bash
  docker-compose up --scale python-app=3
  ```
  这将启动 3 个 `python-app` 容器实例。

### 12. 查看容器使用的卷

```bash
docker-compose volume ls
```
- **作用**：列出当前 `docker-compose` 中定义的卷。

### 13. 删除未使用的卷

```bash
docker-compose down --volumes
```
- **作用**：删除当前服务相关的所有卷，通常是停止并删除服务后清理卷使用的空间。

### 14. 停止某个特定的服务

```bash
docker-compose stop <service_name>
```
- **作用**：停止指定的服务容器。

### 15. 开始某个特定的服务

```bash
docker-compose start <service_name>
```
- **作用**：启动已经停止的指定服务容器。

### 16. 导出容器配置

```bash
docker-compose config
```
- **作用**：验证并查看完整的合并后的配置。对于较复杂的 `docker-compose.yml` 文件，这可以帮助调试和验证配置是否正确。

Docker 网络相关的常见命令包括以下几类操作：创建、查看、连接、断开和删除网络，以及容器与网络的操作。

### 1. **查看网络**
- **列出所有网络**
  ```bash
  docker network ls
  ```

- **查看特定网络的详细信息**
  ```bash
  docker network inspect <network_name_or_id>
  ```

### 2. **创建网络**
- **创建一个默认类型的网络（bridge）**
  ```bash
  docker network create <network_name>
  ```

- **创建一个指定类型的网络**
  - **Bridge 网络**
    ```bash
    docker network create --driver bridge <network_name>
    ```
  - **Overlay 网络**
    ```bash
    docker network create --driver overlay <network_name>
    ```
  - **Host 网络**
    ```bash
    docker network create --driver host <network_name>
    ```
  - **None 网络**
    ```bash
    docker network create --driver none <network_name>
    ```

- **指定子网和网关**
  ```bash
  docker network create --subnet <subnet> --gateway <gateway_ip> <network_name>
  ```

### 3. **连接容器到网络**
- **将运行中的容器连接到网络**
  ```bash
  docker network connect <network_name> <container_name_or_id>
  ```

- **连接容器时指定别名**
  ```bash
  docker network connect --alias <alias_name> <network_name> <container_name_or_id>
  ```

### 4. **断开容器与网络**
- **从网络中断开容器**
  ```bash
  docker network disconnect <network_name> <container_name_or_id>
  ```

### 5. **删除网络**
- **删除网络**
  ```bash
  docker network rm <network_name_or_id>
  ```

- **删除未使用的网络**
  ```bash
  docker network prune
  ```

### 6. **运行容器时指定网络**
- **在启动容器时指定要连接的网络**
  ```bash
  docker run --network <network_name> <image_name>
  ```

这些命令涵盖了 Docker 网络管理的基本操作，方便你在不同的场景下灵活使用。
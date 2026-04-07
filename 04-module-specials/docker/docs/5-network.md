Docker 网络是 Docker 容器之间以及容器与外部世界之间通信的基础。Docker 提供了多种网络模式，方便开发者根据需要选择合适的网络配置。

### Docker 网络的核心概念

1. **网络驱动**：
   Docker 支持多种网络驱动，每种驱动适用于不同的场景。主要的网络驱动包括：
   - **bridge**：默认驱动，适用于在同一主机上隔离容器网络。通常用于容器之间的通信。
   - **host**：直接使用宿主机的网络栈，容器与宿主机共享网络接口，适合对性能要求较高的场景。
   - **overlay**：跨主机通信，适用于集群环境（如 Docker Swarm 或 Kubernetes）。容器可以在不同主机上通过虚拟网络进行通信。
   - **macvlan**：允许为容器分配一个独立的 MAC 地址，使容器能够直接与物理网络设备通信。
   - **none**：没有网络，适用于需要完全隔离的容器。

2. **网络命名空间**：
   每个 Docker 容器都有自己的网络命名空间，这意味着每个容器都有独立的网络接口和路由表。

3. **IP 地址**：
   每个容器在其网络中都有一个唯一的 IP 地址，可以通过该地址与其他容器或外部网络通信。

### 常见 Docker 网络操作

以下是一些常见的 Docker 网络操作命令：

#### 1. 查看网络

列出所有 Docker 网络：
```bash
docker network ls
```

#### 2. 创建网络

使用以下命令创建一个新的 Docker 网络：
```bash
docker network create my-network
```
你可以指定网络驱动：
```bash
docker network create --driver bridge my-network
```

#### 3. 查看网络详细信息

查看某个网络的详细信息：
```bash
docker network inspect my-network
```

#### 4. 删除网络

删除一个网络（确保没有容器使用该网络）：
```bash
docker network rm my-network
```

#### 5. 连接和断开容器

将容器连接到指定网络：
```bash
docker network connect my-network my-container
```

将容器从网络中断开：
```bash
docker network disconnect my-network my-container
```

### Docker 网络模式

#### 1. Bridge 网络

- **使用场景**：默认情况下，Docker 会在创建容器时使用 bridge 网络。这适合在单一主机上隔离和连接多个容器。
- **示例**：
  ```bash
  docker run -d --name my-container --network bridge my-image
  ```

#### 2. Host 网络

- **使用场景**：容器与宿主机共享网络接口，适用于对延迟和带宽要求较高的应用。
- **示例**：
  ```bash
  docker run -d --network host my-image
  ```

#### 3. Overlay 网络

- **使用场景**：在 Docker Swarm 或 Kubernetes 中使用，支持跨主机的容器通信。
- **示例**：
  ```bash
  docker network create -d overlay my-overlay-network
  ```

#### 4. Macvlan 网络

- **使用场景**：适合需要直接与物理网络通信的应用，例如在特定的网络环境中。
- **示例**：
  ```bash
  docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 my-macvlan-network
  ```


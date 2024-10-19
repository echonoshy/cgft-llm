# Docker 镜像相关内容说明

---

## 1. Docker 镜像简介

Docker 镜像是一个只读模板，包含了启动容器所需的文件系统和应用程序。镜像可以基于其他镜像来构建，具有层级结构。每次修改都会创建一个新的镜像层，因此镜像体积通常较小且方便复用。镜像是不可变的，容器运行时是基于镜像创建的，但它们本身不会发生改变。

### 主要特点：
- **只读**：镜像是不可更改的，修改后的内容存储在新的一层中。
- **层级结构**：镜像可以基于其他镜像构建，形成层级式的结构。
- **高效复用**：只需存储和分发不同层的变化。

---

## 2. 查看镜像列表

使用 `docker images` 命令可以查看本地已有的镜像列表。

```bash
docker images
```

输出示例：

```bash
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              2ca708c1c9cc        3 weeks ago         72.9MB
nginx               stable              5b8ec90faaa3        2 months ago        133MB
```

- **REPOSITORY**：镜像的名称。
- **TAG**：镜像的标签，常用于区分不同版本。
- **IMAGE ID**：镜像的唯一标识符。
- **CREATED**：镜像的创建时间。
- **SIZE**：镜像的大小。

---

## 3. 拉取镜像

使用 `docker pull` 命令从 Docker 仓库中拉取镜像。

```bash
docker pull [镜像名]:[标签]
```

示例，拉取 `nginx` 的最新版本镜像：

```bash
docker pull nginx:latest
```

如果不指定标签，则默认拉取 `latest` 标签的镜像。

---

## 4. 构建镜像

通过 `Dockerfile` 可以构建新的镜像。`Dockerfile` 是一个包含一系列指令的文件，定义了如何创建镜像。

### 4.1 创建 Dockerfile

示例 `Dockerfile`，基于 `ubuntu` 镜像并安装 `nginx`：

```Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
CMD ["nginx", "-g", "daemon off;"]
```

### 4.2 构建镜像

在 `Dockerfile` 所在目录下运行以下命令：

```bash
docker build -t my-nginx-image:latest .
```

- `-t`：为新镜像指定名称和标签。
- `.`：指定构建上下文，通常是当前目录。

---

## 5. 为镜像打标签

`docker tag` 命令用于为已有镜像创建新的标签。标签可以帮助我们区分不同的镜像版本或标识。

```bash
docker tag [源镜像名]:[源标签] [目标镜像名]:[目标标签]
```

示例，将 `my-nginx-image:latest` 打标签为 `v1.0`：

```bash
docker tag my-nginx-image:latest my-nginx-image:v1.0
```

---

## 6. 推送镜像到仓库

`docker push` 命令可以将镜像推送到远程 Docker 仓库。

```bash
docker push [镜像名]:[标签]
```

示例，将 `my-nginx-image:v1.0` 推送到 Docker Hub：

```bash
docker push your_dockerhub_username/my-nginx-image:v1.0
```

注意，推送之前需要登录 Docker Hub：

```bash
docker login
```

---

## 7. 从容器创建新镜像

如果你基于某个容器进行了修改，并希望保存这些修改为一个新的镜像，可以使用 `docker commit` 命令。

### 7.1 运行容器并进行修改

```bash
docker run -it ubuntu:latest /bin/bash
```

在容器中进行操作，例如安装新软件：

```bash
apt-get update
apt-get install -y nginx
```

### 7.2 提交容器为新镜像

在退出容器后，使用 `docker commit` 将容器保存为新的镜像：

```bash
docker commit [容器ID或名称] [新镜像名]:[标签]
```

例如：

```bash
docker commit d9b100f2f636 my-custom-ubuntu:v1
```

---

## 8. 删除镜像

使用 `docker rmi` 命令可以删除本地的 Docker 镜像。

```bash
docker rmi [镜像ID或名称]
```

示例：

```bash
docker rmi my-nginx-image:v1.0
```

---

## 9. 导入和导出镜像

### 9.1 导出镜像

`docker save` 可以将镜像导出为一个 tar 文件。

```bash
docker save -o [输出文件名.tar] [镜像名]:[标签]
```

例如：

```bash
docker save -o my-nginx-image.tar my-nginx-image:v1.0
```

### 9.2 导入镜像

`docker load` 可以从一个 tar 文件导入镜像。

```bash
docker load -i [镜像文件名.tar]
```

例如：

```bash
docker load -i my-nginx-image.tar
```

---

## 10. 从文件系统创建镜像

`docker import` 命令用于从文件系统快照（如 tar 文件）中创建镜像。

```bash
docker import [tar文件] [镜像名]:[标签]
```

例如，从 `rootfs.tar` 创建一个新的镜像：

```bash
docker import rootfs.tar my-imported-image:latest
```

---

## 11. 查看镜像历史

使用 `docker history` 可以查看镜像的历史记录，包括每一层是如何构建的。

```bash
docker history [镜像名]:[标签]
```

示例：

```bash
docker history nginx:latest
```

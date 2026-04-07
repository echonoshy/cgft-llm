以下是Docker关于镜像的相关命令：

1. **搜索镜像**：
   ```bash
   docker search [镜像名]
   ```
   例如：`docker search nginx`

2. **下载镜像**：
   ```bash
   docker pull [镜像名]:[标签]
   ```
   例如：`docker pull nginx:latest`

3. **列出本地镜像**：
   ```bash
   docker images [选项]
   ```
   选项：
   • `-a`：列出所有镜像（包括中间层）
   • `-q`：只显示镜像ID
   • `--digests`：显示镜像摘要信息
   • `--no-trunc`：显示完整的镜像信息

4. **删除镜像**：
   ```bash
   docker rmi [镜像ID或镜像名]
   ```
   选项：
   • `-f`：强制删除镜像
   • `-a`：删除所有镜像

5. **构建镜像**：
   ```bash
   docker build -t [镜像名]:[标签] [Dockerfile所在路径]
   ```
   例如：`docker build -t nginx:1.0 .`

6. **导入镜像**：
   ```bash
   docker load -i 镜像保存文件位置
   ```
   例如：`docker load -i /data/nginx.tar`

7. **保存镜像**：
   ```bash
   docker save -o 保存的目标文件名称 镜像名
   ```
   例如：`docker save -o /data/nginx.tar nginx`

8. **给镜像打标签**：
   ```bash
   docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
   ```
   例如：`docker tag nginx 10.10.10.200/software/nginx:1.26`

# docker实现

通过`docker`容器实现`ngrok`服务端

## Dockerfile

```
FROM zjzstu/ubuntu:latest
LABEL Author="zhujian <zjzstu@github.com>"

COPY . /app

WORKDIR /app

ENTRYPOINT ["/app/ngrokd.sh"]
```

将证书/应用以及脚本复制到容器内，执行脚本

## docker-compose.yml

```
version: "3.7"
services:
  ngrok:
    labels:
        AUTHOR: "zhujian <zjzstu@github.com>"
    container_name: ngrokd
    image: zjzstu/ngrok:server
    build: .
    environment:
        - DOMAIN=xxx.xxx.xxx
    ports: 
        - "xxx:xxx"
    restart: always
    tty: true
    stdin_open: true
```

使用`docker-compose`完成镜像创建和启动，指定`ngrok`使用的端口

## 使用

```
# 后台启动
$ docker-compose up -d
```
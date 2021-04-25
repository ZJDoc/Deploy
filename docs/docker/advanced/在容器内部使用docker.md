
# 在容器内部使用docker

## 操作

```
$ docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker --privileged  ubuntu:18.04 bash
```

## 问题

```
$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/containers/json: dial unix /var/run/docker.sock: connect: permission denied
```

## 解决

打开一个新窗口，以`root`身份登录容器

```
$ docker exec -it -u root <xxx> bash
```

创建`docker`组并添加用户

```
$ groupadd docker && usermode -aG docker <user_name>
```

设置普通用户可以操作`docker.sock`

```
$ chmod 777 /var/run/docker.sock
```

## 相关阅读

* [How to use docker from inside Jenkins docker container](https://stackoverflow.com/questions/45447434/how-to-use-docker-from-inside-jenkins-docker-container)
* [在docker容器内部使用docker build](https://blog.csdn.net/vah101/article/details/104973772)
* [Jenkins Environment using Docker](https://joachim8675309.medium.com/jenkins-environment-using-docker-6a12603ebf9)
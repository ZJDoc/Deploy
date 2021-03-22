
# Docker Hub使用

注册表（`registry`）是存储库（`repository`）的集合，存储库是镜像（`image`）的集合，类似于`github`存储库，但代码已经构建

注册表上的帐户可以创建多个存储库。[Docker Hub](https://hub.docker.com)是`Docker`官方的注册表，可用于`Docker`镜像的远程存储和分发

## 登录

首先在`Docker Hub`官网上注册账户，然后在本地登录

```
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: zjykzj
Password: 
WARNING! Your password will be stored unencrypted in /home/zj/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store
```

完成登录后会在`~/.docker/config.json`中保存用户名和密码

```
~/.docker$ cat config.json 
{
	"auths": {
		"https://index.docker.io/v1/": {
			"auth": "emxxxxxxxxxxxxxxxNg=="
		}
	}
```

下次直接`docker login`即可自动登录

## 标记

需要重新标记本地镜像，使其符合远程注册表的命名方式

```
$ docker tag IMAGE username/repository:tag
```

* 参数`IMAGE`表示本地镜像名
* `username`表示账户名
* `repository`表示仓库名
* `tag`是可选的，但可以给定一个意义的标记

比如

```
$ docker tag zjykzj/hello-world:latest zjykzj/hello-world:0.1.0
```

重新标记完成后会生成一个新的镜像名和标记，指向同一个镜像（`ID`相同）

```
$ docker image ls
REPOSITORY                           TAG                                       IMAGE ID            CREATED             SIZE
zjykzj/hello-world                   0.1.0                                     33213d19271a        10 minutes ago      64.2MB
zjykzj/hello-world                   latest                                    33213d19271a        10 minutes ago      64.2MB
```

## 发布

上传已标记的镜像到仓库

```
$ docker push zjykzj/hello-world:0.1.0 
The push refers to repository [docker.io/zjykzj/hello-world]
802d08069c1a: Pushed 
1852b2300972: Mounted from library/ubuntu 
03c9b9f537a4: Mounted from library/ubuntu 
8c98131d2d1d: Mounted from library/ubuntu 
cc4590d6a718: Mounted from library/ubuntu 
0.1.0: digest: sha256:ae8ccd59bc2bc0ff07db5a6df98693182c27cc6c996de8033160ecdc0b8375e1 size: 1359

$ docker push zjykzj/hello-world:latest 
The push refers to repository [docker.io/zjykzj/hello-world]
802d08069c1a: Layer already exists 
1852b2300972: Layer already exists 
03c9b9f537a4: Layer already exists 
8c98131d2d1d: Layer already exists 
cc4590d6a718: Layer already exists 
latest: digest: sha256:ae8ccd59bc2bc0ff07db5a6df98693182c27cc6c996de8033160ecdc0b8375e1 size: 1359
```

完成之后即可在仓库中查看：[zjykzj/hello-world](https://hub.docker.com/repository/docker/zjykzj/hello-world)

**注意：`latest`指向`0.1.0`镜像，但是需要单独上传**

## 拉取

运行镜像`zjykzj/hello-world:0.1.0`，如果本地不存在，则会从远程拉取

```
$ docker run zjykzj/hello-world:0.1.0
Unable to find image 'zjykzj/hello-world:0.1.0' locally
0.1.0: Pulling from zjykzj/hello-world
423ae2b273f4: Already exists 
de83a2304fa1: Already exists 
f9a83bce3af0: Already exists 
b6b53be908de: Already exists 
e422f68af1c3: Pull complete 
Digest: sha256:ae8ccd59bc2bc0ff07db5a6df98693182c27cc6c996de8033160ecdc0b8375e1
Status: Downloaded newer image for zjykzj/hello-world:0.1.0
Hello World
```

## 注销用户

使用命令`docker logout`即可，此时会把配置文件中的加密用户信息删除

```
$ docker logout
Removing login credentials for https://index.docker.io/v1/
:~/.docker$ cat config.json 
{
	"auths": {},
}
```

## 相关阅读

* [Get Started, Part 2: Containers](https://docs.docker.com/get-started/part2/#recap-and-cheat-sheet-optional)
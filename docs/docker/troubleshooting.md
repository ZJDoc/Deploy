
# 问题解答

## 问题一： 安装g++出错

参考：

[Ubuntu18.04LTS安装g++错误以及解决方法](http://blog.sina.com.cn/s/blog_64bb0c990102yv3a.html)

[安装g++出现的问题解决了一部分，还有一些。求大神指教](https://forum.ubuntu.org.cn/viewtopic.php?t=465488)

使用`Docker`镜像`Ubuntu:18.04`，安装`g++`时出现错误

```
The following packages have unmet dependencies:
 g++ : Depends: g++-5 (>= 5.3.1-3~) but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

网上查询时发现可能是系统镜像源设置出错，我使用了`Ubuntu 16.04`的阿里镜像。在[Mirrors](https://opsx.alibaba.com/mirror)中找到`Ubuntu 18.04`的镜像源配置

```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

重新配置后，成功安装`g++`

## 问题二：安装git出错

最新发现：是因为`Ubuntu`镜像源出错，我在`18.04`上误用了`16.04`的`ali mirror`

### 问题

使用`docker`镜像`zjzstu/ubuntu:18.04`，发现无法安装`git`

```
...
...
The following packages have unmet dependencies:
 git : Depends: liberror-perl but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

缺少一系列的`git`依赖，测试多次之后成功安装`git`

### Dockerfile

```
FROM zjzstu/ubuntu:18.04
RUN apt-get update \
	&& apt-get install -y --allow-downgrades openssh-client perl-base=5.22.1-9ubuntu0.6 perl-modules-5.22 libperl5.22 netbase rename perl liberror-perl git
CMD git version 
```

### 镜像

构建镜像

```
$ docker build --no-cache -t zjzstu/ubuntu:18.04-git .
```

运行容器，输出`git`版本号

```
$ docker run zjzstu/ubuntu:18.04-git 
git version 2.7.4
```

上传到[Docker Hub](https://hub.docker.com/r/zjzstu/ubuntu)

## 问题三：docker build运行apt-get update失败

进入`ubuntu:18.04`容器，运行`apt-get update`失败

```
$ docker run -it ubuntu:18.04
root@06f6c91954e1:/# apt-get update
Err:1 http://security.ubuntu.com/ubuntu bionic-security InRelease        
  Temporary failure resolving 'security.ubuntu.com'
Err:2 http://archive.ubuntu.com/ubuntu bionic InRelease                  
  Temporary failure resolving 'archive.ubuntu.com'
Err:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Err:4 http://archive.ubuntu.com/ubuntu bionic-backports InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Reading package lists... Done        
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/bionic/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/bionic-updates/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/bionic-backports/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/bionic-security/InRelease  Temporary failure resolving 'security.ubuntu.com'
W: Some index files failed to download. They have been ignored, or old ones used instead.
root@06f6c91954e1:/# 
```

### 发现问题

测试是否是`DNS`解析出错，测试命令如下：

``` 
$ docker run busybox nslookup baidu.com
nslookup: write to '127.0.1.1': Connection refused
;; connection timed out; no servers could be reached
```

启动镜像`busybox`，使用`nslookup`搜索`baidu.com`对应`IP`，发现没有找到`DNS`服务器

### 解决

参考[SOLVED: Docker build “Could not resolve ‘archive.ubuntu.com’” apt-get fails to install anything](https://medium.com/@faithfulanere/solved-docker-build-could-not-resolve-archive-ubuntu-com-apt-get-fails-to-install-anything-9ea4dfdcdcf2)，默认`Docker`使用`8.8.8.8`作为`DNS`服务器地址，而不是主机的`DNS`服务器地址

搜索主机的`DNS`服务器：

```
$ nmcli dev show | grep 'IP4.DNS'
IP4.DNS[1]:                             192.168.0.1
```

**临时解决方式：参数配置**

```
$ docker run --dns 192.168.0.1 busybox nslookup www.baidu.com
Server:		192.168.0.1
Address:	192.168.0.1:53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com
Name:	www.a.shifen.com
Address: 112.80.248.76
Name:	www.a.shifen.com
Address: 112.80.248.75

*** Can't find www.baidu.com: No answer
```

**永久解决方式：配置Docker守护进程**

修改配置文件`/etc/docker/daemon.json`，添加主机`DNS`服务器后重启`Docker`守护进程

```
{
    "dns": ["192.168.0.1", "8.8.8.8", "8.8.4.4"]
}
```

*后面两个地址是google提供的DNS服务器地址*

```
$ systemctl restart docker

$ docker run busybox nslookup baidu.com
Server:		192.168.0.1
Address:	192.168.0.1:53

Non-authoritative answer:
Name:	baidu.com
Address: 220.181.38.148
Name:	baidu.com
Address: 39.156.69.79

*** Can't find baidu.com: No answer
```

## 问题四：service启动docker失效

```
$ service docker start
Job for docker.service failed because the control process exited with error code. See "systemctl status docker.service" and "journalctl -xe" for details.

$ systemctl status docker.service
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: failed (Result: start-limit-hit) since 四 2019-09-19 16:16:09 CST; 6s ago
     Docs: https://docs.docker.com
  Process: 7950 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock (code=exited, status=1/FAILURE)
 Main PID: 7950 (code=exited, status=1/FAILURE)

9月 19 16:16:07 zj-ThinkPad-T470p systemd[1]: Failed to start Docker Application Container Engine.
9月 19 16:16:07 zj-ThinkPad-T470p systemd[1]: docker.service: Unit entered failed state.
9月 19 16:16:07 zj-ThinkPad-T470p systemd[1]: docker.service: Failed with result 'exit-code'.
9月 19 16:16:09 zj-ThinkPad-T470p systemd[1]: docker.service: Service hold-off time over, scheduling restart.
9月 19 16:16:09 zj-ThinkPad-T470p systemd[1]: Stopped Docker Application Container Engine.
9月 19 16:16:09 zj-ThinkPad-T470p systemd[1]: docker.service: Start request repeated too quickly.
9月 19 16:16:09 zj-ThinkPad-T470p systemd[1]: Failed to start Docker Application Container Engine.
9月 19 16:16:09 zj-ThinkPad-T470p systemd[1]: docker.service: Unit entered failed state.
9月 19 16:16:09 zj-ThinkPad-T470p systemd[1]: docker.service: Failed with result 'start-limit-hit'.
```

我的问题是`/etc/docker/daemon.json`配置出错

```
$ cat /etc/docker/daemon.json 
{
    "mtu": 1450,
    "registry-mirrors": ["https://xxx.mirror.aliyuncs.com"]，
    "dns": ["192.168.0.1", "8.8.8.8"]
}
```

去掉`dns`键值对后重新启动成功

```
$ sudo service docker start
$ ps aux | grep docker
root      8263  2.0  0.5 805596 82912 ?        Ssl  16:19   0:00 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
zj        8468  0.0  0.0  15964  1016 pts/2    R+   16:19   0:00 grep --color=auto docker
```

# [Docker][Ubuntu 18.04]网络工具安装

参考：

[Why isn't ifconfig available in Ubuntu Docker container?](https://serverfault.com/questions/613528/why-isnt-ifconfig-available-in-ubuntu-docker-container)

[ubuntu 容器安装ping ifconfig ip命令](https://www.cnblogs.com/S--S/p/7209682.html)

`Docker`官方`Ubuntu`镜像不包含`ifconfig/ip/ping`，必须手动安装

```
# ifconfig
$ apt-get install net-tools
# ip
$ apt-get install iproute2
# ping
$ apt-get install iputils-ping
```
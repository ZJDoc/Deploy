
# [Ubuntu 18.04]wifi信息查询

在修改本地`DNS`设置的时候无意间发现`wifi`信息查询。从`Ubuntu 18.04`开始使用`netplan`管理网络操作，其配置文件如下：

```
$ pwd
/etc/netplan
$ cat 01-network-manager-all.yaml
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
```

`netplan`利用`NetworkManager`来管理网络相关操作，而`NetworkManager`的配置文件路径位于

```
$ pwd
/etc/NetworkManager
$ ls
conf.d  dispatcher.d  dnsmasq.d  dnsmasq-shared.d  NetworkManager.conf  system-connections
```

进入`system-connections`文件夹，即可发现过往连接过的`wifi`日志
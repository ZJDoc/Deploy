
# netplan

从`Ubuntu 18.04`开始，使用`netplan`统一管理网络配置，其配置文件位于`/etc/netplan`，通过`YAML`文件进行网络配置

默认包含了一个配置文件`01-network-manager-all.yaml`

```
/etc/netplan$ cat 01-network-manager-all.yaml
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
```

关于netplan的使用示例参考[Netplan configuration examples](https://netplan.io/examples)，其具体属性参考[Ubuntu 18.04 网络配置介绍](https://developer.aliyun.com/article/744737)

当前电脑在Wifi环境下，所以配置文件修改如下：

```
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
  # 在wifi环境下配置，在以太网下面使用ethernets
  wifis:
    # 网卡名
    wlp2s0b1:
      # 开启使用ipv4/ipv6的DHCP，默认是关闭
      dhcp4: no
      dhcp6: no
      # 对应网卡配置的静态ip地址，是ip/掩码的格式
      addresses: [192.168.0.184/24]
      # 默认网关
      gateway4: 192.168.0.1
      # 设置DNS服务器
      nameservers:
        addresses: [119.29.29.29, 223.5.5.5, 223.6.6.6]
```

修改完成后执行更新命令

```
$ sudo netplan try
$ sudo netplan apply
```

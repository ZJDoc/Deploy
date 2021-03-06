
# [Ubuntu 18.04][resolv.conf]公共DNS设置

## 为什么要使用公共DNS

* 速度快
* 更稳定
* 无劫持

国内国外都有很多的厂商提供了免费的公共`DNS`，比如：

1. [DNSPod Public DNS](https://www.dnspod.cn/Products/Public.DNS)：`119.29.29.29`
2. [阿里云公共DNS](http://www.alidns.com/index.html?spm=a2chw.13814944.0.0.46ad1760TccxQ0)：`223.5.5.5/223.6.6.6`
3. [Google Public DNS](https://developers.google.com/speed/public-dns)：`8.8.8.8/8.8.4.4`

## /etc/resolv.conf 

`Ubuntu`系统通过读取[/etc/resolv.conf](http://manpages.ubuntu.com/manpages/bionic/man5/resolv.conf.5.html)中的`DNS`地址进行查询，默认`DNS`服务器`IP`是`127.0.0.53`

```
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
# 127.0.0.53 is the systemd-resolved stub resolver.
# run "systemd-resolve --status" to see details about the actual nameservers.

nameserver 127.0.0.53
```

该文件是一个软链接，其指向`/run/systemd/resolve/resolv.conf`

## 如何设置公共DNS

由于`/etc/resolv.conf`会被重写，所以关键问题在于如何在`/etc/resolv.conf`文件中添加新的`DNS`服务器地址

尝试了很多种方式，包括命令`resolvconf`和`netplan`，最后找到一种比较合理的方式

第一步：调整`/etc/resolv.conf`的软链接，使其指向文件`/run/systemd/resolve/resolv.conf`

```
$ cd /etc
$ rm resolv.conf
$ ln -s /run/systemd/resolve/resolv.conf resolv.conf
```

第二步：修改配置文件`/etc/systemd/resolved.conf`，添加新的`DNS`服务器`IP`

```
$ cat resolved.conf 
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.
#
# Entries in this file show the compile time defaults.
# You can change settings by editing this file.
# Defaults can be restored by simply deleting this file.
#
# See resolved.conf(5) for details

[Resolve]
DNS=119.29.29.29 223.5.5.5 223.6.6.6 
#DNS=
#FallbackDNS=
#Domains=
#LLMNR=no
#MulticastDNS=no
#DNSSEC=no
#Cache=yes
#DNSStubListener=yes
```

第三步：重启系统

完成后，可以查看新的`/etc/resolv.conf`配置

```
$ cat /etc/resolv.conf
# This file is managed by man:systemd-resolved(8). Do not edit.
#
# This is a dynamic resolv.conf file for connecting local clients directly to
# all known uplink DNS servers. This file lists all configured search domains.
#
# Third party programs must not access this file directly, but only through the
# symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a different way,
# replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 119.29.29.29
nameserver 223.5.5.5
nameserver 223.6.6.6
# Too many DNS servers configured, the following entries may be ignored.
nameserver 113.214.230.25
nameserver 113.215.2.222
```

使用命令`systemd-resolve --status`查询

```
$ systemd-resolve --status
Global
         DNS Servers: 119.29.29.29
                      223.5.5.5
                      223.6.6.6
。。。
。。。
```

使用命令`nslookup`解析网址：

```
$ nslookup www.baidu.com
Server:		119.29.29.29
Address:	119.29.29.29#53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com.
Name:	www.a.shifen.com
Address: 182.61.200.7
Name:	www.a.shifen.com
Address: 182.61.200.6
```

## 相关阅读

* [为什么要使用 Public DNS ？](https://www.dnspod.cn/Products/Public.DNS)
* [ubuntu18.04 dsn 重启就会重置该怎么办？](https://segmentfault.com/q/1010000015091523)
* [Ubuntu 18.04的DNS问题(已解决)](https://my.oschina.net/u/2306127/blog/1930116)
* [ubuntu18.04直接更改/etc/resolv.conf修改nameserver重启被重置解决方法](https://blog.csdn.net/lengye7/article/details/88877867)
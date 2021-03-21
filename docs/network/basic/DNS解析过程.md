
# DNS解析过程

`DNS`解析过程就是将域名转换成`IP`地址的过程

## DNS简介

`DNS`(`Domain Name System`，称为域名系统)，是一种组织成域层次结构的计算机和网络服务命名系统，它作用于`TCP/IP`网络，所提供的服务是用来将主机名和域名转换为`IP`地址的工作

## 解析过程

浏览器从`URL`中解析出`host`字段后，依次按如下顺序进行查询：

1. 从浏览器缓存中查找是否有该域名对应的IP地址。如果没有访问过该域名或者缓存已清空，则使用第二步
2. 查询系统缓存，从`hosts`文件中查找是否存在该域名以及对应`IP`。如果不存在，使用第三步
3. 查询路由器缓存

以上`3`步均在`DNS`客户端完成，后续操作将请求域名服务器

## /etc/hosts

`hosts`文件是`linux`系统中负责`ip`地址与域名快速解析的文件，`DNS`客户端首先查询缓存，然后查询`hosts`文件，最后查询`DNS`服务器

`Ubuntu`中的文件地址为`/etc/hosts`

```
$ cat /etc/hosts
127.0.0.1	localhost
127.0.1.1	zj-ThinkPad-T470p

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

0.0.0.0 account.jetbrains.com
```

每行表示一条域名解析，其格式为

```
ip地址 主机名/域名 [主机别名]
```

## 相关阅读

* [面试官:讲讲DNS的原理？](https://zhuanlan.zhihu.com/p/79350395)

* [DNS原理及解析过程详解](https://zhuanlan.zhihu.com/p/88260838)

* [DNS解析全过程分析](https://www.cnblogs.com/kongtongshu/p/11069559.html)

* [linux环境下/etc/hosts文件详解](https://www.jianshu.com/p/476a92a39b45)
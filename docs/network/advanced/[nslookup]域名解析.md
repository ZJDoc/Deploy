
# [nslookup]域名解析

参考：

[nslookup](https://en.wikipedia.org/wiki/Nslookup)

[nslookup(1) - Linux man page](https://linux.die.net/man/1/nslookup)

`nslookup`是一个域名解析工具，用于查询域名对应的`IP`地址

有两种使用方式

1. 交互式（`interactive`）
2. 非交互式（`non-interactive`）

## 安装

```
$ sudo apt install dnsutils
```

## 交互式

首先输入`nslookup`，然后按回车键进入交互界面，再输入相应的域名即可查询对应`IP`，输入`exit`退出

```
$ nslookup 
> www.baidu.com
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com.
Name:	www.a.shifen.com

## Address: 112.80.248.75
Name:	www.a.shifen.com
Address: 112.80.248.76
> 
> www.google.com
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
Name:	www.google.com
Address: 173.252.73.48
> exit
```

## 非交互式

在`nslookup`后跟域名即可

```
$ nslookup www.zhujian.tech
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
Name:	www.zhujian.tech
Address: 148.70.133.9
```
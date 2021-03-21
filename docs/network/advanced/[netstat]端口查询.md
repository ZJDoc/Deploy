
# [netstat]端口查询

使用命令`netstat`进行端口查询

## 查询被占用的端口

```
$ sudo netstat -lnp | grep xxx
```

比如查询占用`1080`的进程

```
$ sudo netstat -lnp | grep 1080
tcp        0      0 127.0.0.1:1080          0.0.0.0:*               LISTEN      5482/python     
udp        0      0 127.0.0.1:1080          0.0.0.0:*                           5482/python
```

端口`1080`被进程`id`为`5482`的应用占据，查询该应用并`kill`

```
$ ps aux | grep 5482
root      5482  0.0  0.0  48020 11940 ?        Ss   18:10   0:00 python local.py -d start
zj        8708  0.0  0.0  15964  1020 pts/21   S+   18:51   0:00 grep --color=auto 5482
$ sudo kill 5482
```
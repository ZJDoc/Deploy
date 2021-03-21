
# [nc]远程端口查询

参考：

[Linux测试远程端口是否开放](https://blog.csdn.net/calmboy_/article/details/89455925)

[Linux nc命令](https://www.runoob.com/linux/linux-comm-nc.html)

## 使用

```
nc -vz [-w <超时秒数>] host port
```

* 参数`-v`表示显示指令执行过程
* 参数`-z`表示使用`0`输入/输出模式，只在扫描通信端口时使用

指定远程地址`host`，以及端口号`port`（*可以指定某一范围内的端口*）

默认使用`tcp`进行检测，如果需要`udp`， 设置参数`-u`

## 示例

测试单个端口号

```
$ nc -vz 148.xxx.xxx.9 12xxx
Connection to 148.70.133.9 12xxx port [tcp/*] succeeded!
```

测试连续多个端口号

```
$ nc -vz -w 2 148.xxx.xxx.9 12344-12346
nc: connect to 148.70.133.9 port 12344 (tcp) timed out: Operation now in progress
Connection to 148.70.133.9 12345 port [tcp/*] succeeded!
nc: connect to 148.70.133.9 port 12346 (tcp) failed: Connection refused
```
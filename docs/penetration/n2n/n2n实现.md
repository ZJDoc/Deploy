
# n2n实现

## 安装

下载[ntop/n2n](https://github.com/ntop/n2n)源码

```
git clone https://github.com/ntop/n2n.git
```

安装其他库

```
$ sudo apt-get install cmake make libssl-dev
```

切换到`v2`版本

```
$ git checkout -b 2.4-stable origin/2.4-stable
Branch 2.4-stable set up to track remote branch 2.4-stable from origin.
Switched to a new branch '2.4-stable'
```

链接、编译和安装

```
$ cmake .
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libssl.so;/usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.0.2g") 
CMake Warning (dev) at CMakeLists.txt:79 (add_executable):
  Policy CMP0037 is not set: Target names should not be reserved and should
  match a validity pattern.  Run "cmake --help-policy CMP0037" for policy
  details.  Use the cmake_policy command to set the policy and suppress this
  warning.

  The target name "test" is reserved or not valid for certain CMake features,
  such as generator expressions, and may result in undefined behavior.
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Configuring done
-- Generating done
-- Build files have been written to: /home/ubuntu/n2n

$ make
Scanning dependencies of target doc
[ 11%] Built target doc
Scanning dependencies of target n2n
[ 15%] Building C object CMakeFiles/n2n.dir/n2n.c.o
[ 19%] Building C object CMakeFiles/n2n.dir/n2n_keyfile.c.o
[ 23%] Building C object CMakeFiles/n2n.dir/edge_utils.c.o
[ 26%] Building C object CMakeFiles/n2n.dir/wire.c.o
[ 30%] Building C object CMakeFiles/n2n.dir/minilzo.c.o
[ 34%] Building C object CMakeFiles/n2n.dir/twofish.c.o
[ 38%] Building C object CMakeFiles/n2n.dir/transform_null.c.o
[ 42%] Building C object CMakeFiles/n2n.dir/transform_tf.c.o
[ 46%] Building C object CMakeFiles/n2n.dir/transform_aes.c.o
[ 50%] Building C object CMakeFiles/n2n.dir/tuntap_freebsd.c.o
[ 53%] Building C object CMakeFiles/n2n.dir/tuntap_netbsd.c.o
[ 57%] Building C object CMakeFiles/n2n.dir/tuntap_linux.c.o
[ 61%] Building C object CMakeFiles/n2n.dir/tuntap_osx.c.o
[ 65%] Building C object CMakeFiles/n2n.dir/version.c.o
[ 69%] Linking C static library libn2n.a
[ 69%] Built target n2n
Scanning dependencies of target supernode
[ 73%] Building C object CMakeFiles/supernode.dir/sn.c.o
[ 76%] Linking C executable supernode
[ 76%] Built target supernode
Scanning dependencies of target edge
[ 80%] Building C object CMakeFiles/edge.dir/edge.c.o
[ 84%] Linking C executable edge
[ 84%] Built target edge
Scanning dependencies of target benchmark
[ 88%] Building C object CMakeFiles/benchmark.dir/benchmark.c.o
[ 92%] Linking C executable benchmark
[ 92%] Built target benchmark
Scanning dependencies of target test
[ 96%] Building C object CMakeFiles/test.dir/test.c.o
[100%] Linking C executable test
[100%] Built target test
ubuntu@VM-16-15-ubuntu:~/n2n$ make install
[ 11%] Built target doc
[ 69%] Built target n2n
[ 76%] Built target supernode
[ 84%] Built target edge
[ 92%] Built target benchmark
[100%] Built target test

$ sudo make install
[ 11%] Built target doc
[ 69%] Built target n2n
[ 76%] Built target supernode
[ 84%] Built target edge
[ 92%] Built target benchmark
[100%] Built target test
Install the project...
-- Install configuration: ""
-- Installing: /usr/local/sbin/edge
-- Installing: /usr/local/sbin/supernode
-- Installing: /usr/share/man8/edge.8.gz
-- Installing: /usr/share/man1/supernode.1.gz
-- Installing: /usr/share/man7/n2n.7.gz
```

## 配置

当前有`3`台电脑

1. 局域网服务器`A`
2. 腾讯云服务器`B`
3. 自己笔记本`C`

`B`作为服务器端，启动`supernode`

```
$ supernode -l 3307 -v
```

* `-l`表示`UDP`监听端口
* `-v`表示详细输出

`A`和`C`作为客户端，启动`edge`

```
# A操作
$ sudo edge -d n2n0 -c mynetwork -k encryptme -a 172.16.0.200 -l a.b.c.d:3307 -M 1200 -m ae:e0:4f:e7:47:5c
# C操作
$ sudo edge -d n2n0 -c mynetwork -k encryptme -a 172.16.0.201 -l a.b.c.d:3307 -M 1200 -m ae:e0:4f:e7:47:5b
```

* `-d`表示新建虚拟网卡名
* `-c`表示`n2n`社区名
* `-k`表示加密键值
* `-a`表示自定义`ip`
* `-l`表示服务器`ip:`监听端口
* `-M`表示虚拟网卡最大传输单位
* `-m`表示虚拟网卡`MAC`地址

### 调试边缘节点

添加参数`-v`和`-f`

* `-f`表示在前台运行`edge`而不是作为守护进程
* `-v`表示详细输出

### 终止边缘节点

查询`pid`并终止

```
$ ps aux | grep edge
root     28348  0.0  0.0  10888   316 ?        Ss   15:50   0:00 edge -d n2n0 -c xxx
zj       29947  0.0  0.0  15964  1016 pts/23   S+   16:09   0:00 grep --color=auto edge
$ sudo kill -9 28348
```

### 稳定性

隔一段时间`ping`内网服务器会发现无法连接 

```
PING 172.16.0.200 (172.16.0.200) 56(84) bytes of data.
From 172.16.0.201 icmp_seq=1 Destination Host Unreachable
```

参考[搜集整理N2N使用中的一些经验](http://www.lucktu.com/archives/767.html)，是因为`edge`休眠了，持续一段时间就能够`ping`通了

```
$ ping 172.16.0.200
PING 172.16.0.200 (172.16.0.200) 56(84) bytes of data.
From 172.16.0.201 icmp_seq=1 Destination Host Unreachable
From 172.16.0.201 icmp_seq=2 Destination Host Unreachable
From 172.16.0.201 icmp_seq=3 Destination Host Unreachable
From 172.16.0.201 icmp_seq=4 Destination Host Unreachable
From 172.16.0.201 icmp_seq=5 Destination Host Unreachable
From 172.16.0.201 icmp_seq=6 Destination Host Unreachable
From 172.16.0.201 icmp_seq=7 Destination Host Unreachable
From 172.16.0.201 icmp_seq=8 Destination Host Unreachable
From 172.16.0.201 icmp_seq=9 Destination Host Unreachable
From 172.16.0.201 icmp_seq=10 Destination Host Unreachable
From 172.16.0.201 icmp_seq=11 Destination Host Unreachable
From 172.16.0.201 icmp_seq=12 Destination Host Unreachable
From 172.16.0.201 icmp_seq=13 Destination Host Unreachable
64 bytes from 172.16.0.200: icmp_seq=14 ttl=64 time=1200 ms
64 bytes from 172.16.0.200: icmp_seq=15 ttl=64 time=176 ms
64 bytes from 172.16.0.200: icmp_seq=16 ttl=64 time=87.6 ms
64 bytes from 172.16.0.200: icmp_seq=17 ttl=64 time=99.2 ms
64 bytes from 172.16.0.200: icmp_seq=18 ttl=64 time=87.2 ms
64 bytes from 172.16.0.200: icmp_seq=19 ttl=64 time=88.7 ms
64 bytes from 172.16.0.200: icmp_seq=20 ttl=64 time=88.6 ms
^C
--- 172.16.0.200 ping statistics ---
20 packets transmitted, 7 received, +13 errors, 65% packet loss, time 19311ms
rtt min/avg/max/mdev = 87.257/261.182/1200.246/384.543 ms, pipe 4
```

## 相关阅读

* [n2n内网穿透打洞部署全过程 + nginx公网端口映射](https://cloud.tencent.com/developer/article/1120865)

* [如何在 Linux 上配置点对点 VPN](https://linux.cn/article-4608-1.html)

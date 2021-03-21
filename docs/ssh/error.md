
# ERROR

## 问题一：agent refused operation Permission denied (publickey) Error

参考：[git使用错误记录及解决](https://segmentfault.com/a/1190000008733238)

私钥没有添加到缓存

    $ eval "$(ssh-agent -s)"
    $ ssh-add 指定私钥文件

## 问题二：known_hosts

参考：[What is the difference between authorized_keys and known_hosts file for SSH?](https://security.stackexchange.com/questions/20706/what-is-the-difference-between-authorized-keys-and-known-hosts-file-for-ssh)

`known_hosts`存放在`~/.ssh`文件夹内，用于保存已连接过的服务器公钥，其目的是确保服务器连接的安全性，第一次连接时需要会询问你是否添加到

搜索已经连接过的服务器公钥

    $ ssh-keygen -F hostname [-f known_hosts_file] [-l]

    $ ssh-keygen -F 132.232.142.219
    # Host 132.232.142.219 found: line 10 
    |1|pi+zsVaxd0uefX2luX9dfHymHok=|HIEJX3xNsPOqV31fvg3nIfRkfmE= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItb...

当服务器重装后，会生成新的服务器公钥，需要删除客户端当前公钥然后重新设置

    # 错误消息
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
    Someone could be eavesdropping on you right now (man-in-the-middle attack)!
    It is also possible that a host key has just been changed.
    The fingerprint for the ECDSA key sent by the remote host is
    SHA256:8eHlAUPZtTc6WT+dXP4RHYw7fO8hO4lpzOH89hPUOR8.
    Please contact your system administrator.
    Add correct host key in /home/zj/.ssh/known_hosts to get rid of this message.
    Offending ECDSA key in /home/zj/.ssh/known_hosts:10
    remove with:
    ssh-keygen -f "/home/zj/.ssh/known_hosts" -R 132.232.142.219
    ECDSA host key for 132.232.142.219 has changed and you have requested strict checking.
    Host key verification failed.

删除本地存储公钥

    $ ssh-keygen -f "/home/zj/.ssh/known_hosts" -R 132.232.142.219
    # Host 132.232.142.219 found: line 10
    /home/zj/.ssh/known_hosts updated.
    Original contents retained as /home/zj/.ssh/known_hosts.old

## 问题三：客户端连接一段时间后卡死问题解决

在`Ubuntu`下经常需要通过`SSH`进行远程连接，使用过程中往往会遇到一个问题，就是命令行窗口在经过一段时间后就会卡死，无法输入命令

参考：

[连接远程ssh老是掉线解决办法](https://blog.csdn.net/qq_39846820/article/details/103371782)

[Linux下ssh连接时间过长客户端卡死问题](https://blog.csdn.net/zhangwei_2010/article/details/105239604)

其解决方案是通过定时发送心跳响应，保证客户端和服务器之间的连接

### 修改客户端

在客户端上修改文件`/etc/ssh/ssh_config`，添加如下内容：

```
# 添加
ServerAliveInterval 20
ServerAliveCountMax 999
```

每隔`20s`向服务器发送一次心跳；若超过`999`次请求都没有发送成功，则主动断开与服务器端的连接

### 修改服务端

在服务器上修改文件`/etc/ssh/sshd_config`，添加如下内容：

```
# 添加
ClientAliveInterval 30
ClientAliveCountMax 10
```

每隔`30s`向客户端发送一次心跳；若超过`10`次请求都没有发送成功，则主动断开与客户端的连接

### 更新

可同时修复上述两项配置文件，完成后重启`ssh`服务

```
# 重启客户端
$ sudo systemctl restart ssh
# 重启服务端
$ sudo systemctl restart sshd
```

## 问题四：连接卡住

使用`ssh`远程连接卡住，打印详细信息如下：

```
。。。
。。。
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256@libssh.org
debug1: kex: host key algorithm: ecdsa-sha2-nistp256
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
```

解决方法是重新删除`~/.ssh/known_hosts`保存的服务器公钥

```
$ ssh-keygen -f "/home/zj/.ssh/known_hosts" -R 207.xxx.xx.97
```

## 问题五：Too many ssh failures

昨天不小心删除了`ubuntu`用户，导致系统无法登录

今天重装了系统，使用公共镜像`Ubuntu 18.04`，重装完成后进行登录发现如下错误

    $ ssh ubuntu@132.232.142.219
    Received disconnect from 132.232.142.219 port 22:2: Too many authentication failures
    Connection to 132.232.142.219 closed by remote host.
    Connection to 132.232.142.219 closed.

### 解决

先到控制台的云服务器页面，选择左侧的`SSH`密钥选项，删除之前设置的密钥

然后关闭实例，重新设置密钥，输入本地的公钥内容，再次启动实例后就能够登录了

### 调试

使用参数`-v`能够打印出登录进度的调试信息

    $ ssh -v ubuntu@132.232.142.219
    OpenSSH_7.2p2 Ubuntu-4ubuntu2.7, OpenSSL 1.0.2g  1 Mar 2016
    debug1: Reading configuration data /etc/ssh/ssh_config
    debug1: /etc/ssh/ssh_config line 19: Applying options for *
    debug1: Connecting to 132.232.142.219 [132.232.142.219] port 22.
    debug1: Connection established.
    debug1: identity file /home/zj/.ssh/id_rsa type 1
    debug1: key_load_public: No such file or directory
    debug1: identity file /home/zj/.ssh/id_rsa-cert type -1
    debug1: key_load_public: No such file or directory
    debug1: identity file /home/zj/.ssh/id_dsa type -1
    debug1: key_load_public: No such file or directory
    debug1: identity file /home/zj/.ssh/id_dsa-cert type -1
    debug1: key_load_public: No such file or directory
    debug1: identity file /home/zj/.ssh/id_ecdsa type -1
    debug1: key_load_public: No such file or directory
    debug1: identity file /home/zj/.ssh/id_ecdsa-cert type -1
    debug1: key_load_public: No such file or directory
    debug1: identity file /home/zj/.ssh/id_ed25519 type -1
    debug1: key_load_public: No such file or directory
    debug1: identity file /home/zj/.ssh/id_ed25519-cert type -1
    debug1: Enabling compatibility mode for protocol 2.0
    debug1: Local version string SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.7
    debug1: Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4
    debug1: match: OpenSSH_7.6p1 Ubuntu-4 pat OpenSSH* compat 0x04000000
    debug1: Authenticating to 132.232.142.219:22 as 'ubuntu'
    debug1: SSH2_MSG_KEXINIT sent
    debug1: SSH2_MSG_KEXINIT received
    debug1: kex: algorithm: curve25519-sha256@libssh.org
    debug1: kex: host key algorithm: ecdsa-sha2-nistp256
    debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
    debug1: Server host key: ecdsa-sha2-nistp256 SHA256:Jo/TLQ//NbUA3Sg3iZy3glGFLpf26BJtUOmBNMOtfdo
    debug1: Host '132.232.142.219' is known and matches the ECDSA host key.
    debug1: Found key in /home/zj/.ssh/known_hosts:12
    debug1: rekey after 134217728 blocks
    debug1: SSH2_MSG_NEWKEYS sent
    debug1: expecting SSH2_MSG_NEWKEYS
    debug1: SSH2_MSG_NEWKEYS received
    debug1: rekey after 134217728 blocks
    debug1: SSH2_MSG_EXT_INFO received
    debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521>
    debug1: SSH2_MSG_SERVICE_ACCEPT received
    debug1: Authentications that can continue: publickey
    debug1: Next authentication method: publickey
    debug1: Offering RSA public key: /home/zj/.ssh/id_rsa
    debug1: Authentications that can continue: publickey
    debug1: Offering RSA public key: gitee.com
    debug1: Authentications that can continue: publickey
    debug1: Offering RSA public key: github.com
    debug1: Authentications that can continue: publickey
    debug1: Offering RSA public key: zj@zj-ThinkPad-T470p
    debug1: Authentications that can continue: publickey
    debug1: Offering RSA public key: coding.com
    debug1: Authentications that can continue: publickey
    debug1: Offering RSA public key: zj@zj-ThinkPad-T470p
    debug1: Server accepts key: pkalg rsa-sha2-512 blen 279
    debug1: Authentication succeeded (publickey).
    Authenticated to 132.232.142.219 ([132.232.142.219]:22).
    ...
    ...

上述调试信息是修改后的认证成功信息，可以看出`ssh`会遍历`~/.ssh`目录下的私钥文件，所以最开始的`Too many authentication failures`表明服务器端设置了认证的次数，可以通过配置文件修改

    $ cat /etc/ssh/sshd_config  | grep MaxAuth
    #MaxAuthTries 6

### 配置

比如修改`ssh`服务端配置文件`/etc/ssh/sshd_config`，设置认证次数为`100`次，然后重启服务端即可

```
$ sudo vim /etc/ssh/sshd_config
MaxAuthTries 100
$ service sshd restart
```

## 问题六：ssh: connect to host github.com port 22: Connection timed out

今天突然无法访问`github`，出现下面问题：

```
$ ssh -vT git@github.com
。。。
ssh: connect to host github.com port 22: Connection timed out
```

参考[ssh: connect to host github.com port 22: Connection timed out](https://stackoverflow.com/questions/15589682/ssh-connect-to-host-github-com-port-22-connection-timed-out)和[Using SSH over the HTTPS port](https://help.github.com/en/articles/using-ssh-over-the-https-port)

新建文件`~/.ssh/config`，添加如下内容：

```
$ cat config 
Host github.com
	Hostname ssh.github.com
	Port 443
```

重新测试成功

```
$ ssh -T git@github.com
Hi zjZSTU! You've successfully authenticated, but GitHub does not provide shell access.
```

## 问题七：Bad owner or permissions on .ssh config

### 问题复现

```
$ git push origin dev 
Bad owner or permissions on /home/zj/.ssh/config
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

### 问题解决

参考：[Bad owner or permissions on .ssh/config的解决](https://blog.csdn.net/zcc_heu/article/details/79017606)

设置`config`文件权限为`600`即可

```
$ chmod 600 config 
```

## 问题八：ssh_exchange_identification: Connection closed by remote host

连接远程服务器时，老是连接失败

```
$ ssh -p 12xxx zj@xxx.xxx.xxx -vv
OpenSSH_7.2p2 Ubuntu-4ubuntu2.8, OpenSSL 1.0.2g  1 Mar 2016
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: Applying options for *
debug2: resolving "ngrok.zhujian.tech" port 12346
debug2: ssh_connect_direct: needpriv 0
debug1: Connecting to ngrok.zhujian.tech [148.70.133.9] port 12346.
debug1: Connection established.
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_rsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_rsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_dsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_dsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_ecdsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_ecdsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_ed25519 type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/lab305/.ssh/id_ed25519-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8
ssh_exchange_identification: Connection closed by remote host
```

网上有很多的解答，参考

[ssh问题：ssh_exchange_identification: Connection closed by remote host](https://www.cnblogs.com/gaobo543013306/p/9382867.html)

[大量远程ssh连接请求--造成拒绝服务的问题](https://cloud.tencent.com/developer/article/1055038)

[ssh连接提示 "Connection closed by remote host"](https://blog.csdn.net/mjm26/article/details/52242398/)

当前我的问题则是服务器没有装`openssh-server`

```
$ sudo apt install openssh-server
```

## 问题九：Permission denied (publickey)

### 问题描述

使用`Docker Jenkins`，在本地生成私钥，把公钥放置到远程，还是出现了权限错误：

```
$ git ls-remote -h -- git@x48.xx.xx.9:/data/repositories/xxx.git HEAD
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
```

### 解决一

参考[[ssh-add]添加私钥缓存](./[ssh-add]添加私钥缓存.md)和[[ssh-agent]代理设置]([ssh-agent]代理设置.md)，使用工具`ssh-agent`设置代理即可

### 解决二

设置私钥文件为`600`权限（**很重要!!!**）

## 问题十：/etc/ssh/ssh_config: terminating, 1 bad configuration options

### 问题复现

使用`ssh`登录远程服务器，遇到如下问题：

```
$ ssh root@47.240.173.235 -vv
OpenSSH_7.2p2 Ubuntu-4ubuntu2.4, OpenSSL 1.0.2g  1 Mar 2016
debug1: Reading configuration data /etc/ssh/ssh_config
/etc/ssh/ssh_config: line 1: Bad configuration option: maxstartups
debug1: /etc/ssh/ssh_config line 19: Applying options for *
/etc/ssh/ssh_config: terminating, 1 bad configuration options
```

尝试使用`git`克隆远程仓库，也遇到以下问题

```
$ git clone git@47.xxx.xxx.235:/data/repositories/hello.git
Cloning into 'hello'...
/etc/ssh/ssh_config: line 1: Bad configuration option: maxstartups
/etc/ssh/ssh_config: terminating, 1 bad configuration options
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

### 问题解析

参考：[ssh: Bad configuration option: usedns](https://www.cnblogs.com/minglee/p/11210203.html)

搜索`/etc/ssh/ssh_config`，第一行内容如下：

```
/etc/ssh$ cat ssh_config 
MaxStartups 100
...
```

上面这个命令是为了扩大服务端`ssh`的连接限制而添加的。又搜索了`sshd_config`文件，发现如下内容：

```
$ cat sshd_config | grep Max -i
#MaxStartups 10:30:60
```

所以之前的修改错了，取消`ssh_config`中的修改；将`MaxStartups 30`重新添加到`sshd_config`

```
$ cat sshd_config | grep Max -i
MaxStartups 30
#MaxStartups 10:30:60
```

重启`ssh/sshd`

```
$ sudo systemctl restart ssh
$ sudo systemctl restart sshd
```

# [ssh-add]添加私钥缓存

最近腾讯云服务器到期了，重新买了一个实例，在云上创建了一对密钥，将私钥下载到本地，放置在`~/.ssh`文件夹

远程连接时出错：

```
$ ssh ubuntu@148.70.117.214 -v
OpenSSH_7.2p2 Ubuntu-4ubuntu2.8, OpenSSL 1.0.2g  1 Mar 2016
debug1: Reading configuration data /home/zj/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
。。。
。。。
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering RSA public key: /home/zj/.ssh/id_rsa
debug1: Authentications that can continue: publickey
debug1: Trying private key: /home/zj/.ssh/id_dsa
debug1: Trying private key: /home/zj/.ssh/id_ecdsa
debug1: Trying private key: /home/zj/.ssh/id_ed25519
debug1: No more authentication methods to try.
Permission denied (publickey).
```

参考[用ssh登陆服务器(腾讯云)提示permission denied(public key)](https://segmentfault.com/q/1010000004905628)，用`ssh-add`将私钥添加到缓存中

```
$ ssh-add tencent_id_rsa 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'tencent_id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
```

提示私钥`tencent_id_rsa`的权限太大了，所以先修改权限再添加

```
$ chmod 600 tencent_id_rsa
$ ssh-add tencent_id_rsa 
Identity added: tencent_id_rsa (tencent_id_rsa)
```

最后重新连接成功

```
$ ssh ubuntu@148.70.117.214 -v
...
...
debug1: Offering RSA public key: tencent_id_rsa
debug1: Server accepts key: pkalg rsa-sha2-512 blen 151
debug1: Authentication succeeded (publickey).
Authenticated to 148.70.117.214 ([148.70.117.214]:22).
...
...
Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-54-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Sep 26 14:40:46 CST 2019

  System load:  0.05              Processes:           89
  Usage of /:   4.6% of 49.15GB   Users logged in:     0
  Memory usage: 15%               IP address for eth0: 172.27.16.16
  Swap usage:   0%

 * MicroK8s 1.15 is out! Thanks to all 40 contributors, you get the latest
   greatest upstream Kubernetes in a single package.

     https://github.com/ubuntu/microk8s

Last login: Thu Sep 26 14:31:20 2019 from 101.68.71.72
```

## 查询缓存私钥

```
$ ssh-add -l
4096 SHA256:fmK9Jxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxcs /var/jenkins_home/.ssh/zj_rsa (RSA)
```

## 删除缓存私钥

```
$ ssh-add -D
All identities removed.
```
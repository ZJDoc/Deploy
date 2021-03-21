
# [SSH]远程连接

[SSH(Secure Shell)](https://help.ubuntu.com/community/SSH)是一个远程访问和数据传输的安全协议，其相比与`TELNET`等协议，它能够加密用户密码和数据，保证安全传输

[OpenSSH](https://baike.baidu.com/item/OpenSSH)是基于`SSH`协议实现的开源软件，包括了`ssh`(远程连接)、`scp`(远程传输)等等工具

## 安装

查看当前是否已运行`ssh`

    $ ps -aux | grep ssh

安装客户端

    sudo apt-get install openssh-client

安装服务端

    sudo apt-get install openssh-server

## 配置文件

系统配置文件在路径`/etc/ssh`文件夹下

    # 客户端配置
    ssh_config
    # 服务器设置
    sshd_config

里面列出了一些默认配置信息，比如使用端口号为`22`

也可以在用户路径下`~/.ssh/`新建配置文件`config`

如果修改配置文件需要重启服务

    $ sudo service ssh restart
    # 或
    $ sudo systemctl restart ssh

## 远程连接

使用`ssh`命令进行远程连接

    $ ssh
    usage: ssh [-1246AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
            [-D [bind_address:]port] [-E log_file] [-e escape_char]
            [-F configfile] [-I pkcs11] [-i identity_file] [-L address]
            [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
            [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
            [-w local_tun[:remote_tun]] [user@]hostname [command]

### 密码连接

最简单的连接格式，输入登录名和主机地址，然后输入登录密码即可

    ssh user@hostname
    
指定端口号

    ssh -p port [user@]hostname 

指定登录名

    ssh -l login_name hostname

#### 禁止密码连接

参考：[Disable Password Authentication](https://help.ubuntu.com/community/SSH/OpenSSH/Configuring#disable-password-authentication)

### 密钥连接

首先本地生成公钥和私钥，参考[[SSH]生成密钥](./[SSH]生成密钥.md)

    $ ssh-keygen -t rsa -b 4096 -C "132.232.142.219" -f ~/.ssh/tencent_id_rsa
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /home/zj/.ssh/tencent_id_rsa.
    Your public key has been saved in /home/zj/.ssh/tencent_id_rsa.pub.
    The key fingerprint is:
    SHA256:VJGQlDH
    ...
    ...

有两种方法将公钥传输到远程服务器

1. 使用命令`ssh-copy-id`

        ssh-copy-id <username>@<host>

2. 复制公钥到服务器`authorized_keys`文件

        $ pwd
        /home/ubuntu/.ssh
        $ file authorized_keys 
        authorized_keys: OpenSSH RSA public key

如果没有`authorized_keys`文件就新建，将公钥内容复制到上面

## 相关阅读

* [OpenSSH Server](https://help.ubuntu.com/lts/serverguide/openssh-server.html.en)
* [How to Enable SSH on Ubuntu (18.04, 17.04, 16.04, 14.04 etc.)](https://thishosting.rocks/how-to-enable-ssh-on-ubuntu/)
* [How To Use SSH to Connect to a Remote Server in Ubuntu ](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu)
* [SSH/OpenSSH/Keys](https://help.ubuntu.com/community/SSH/OpenSSH/Keys)
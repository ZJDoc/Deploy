
# [SSH]客户端配置文件

`ssh`除了命令行配置参数外，还可以通过配置文件来辅助管理，有两个级别的配置文件

* 用户级(`user-specific file`)：`~/.ssh/config`，通常不存在，如果需要自己新建
* 系统级(`system-wide file`)：`/etc/ssh/ssh_config`，内置有一些默认配置

## 访问权限

用户配置文件的访问权限设置为用户可读可写，组和其他不能操作

    $ sudo chmod 600 ~/.ssh/config

## 优先级

参数数据解析顺序如下：

1. 命令行选项
2. 用户配置文件
3. 系统配置文件

所有的配置选项仅第一次设置有效，所以可以将默认值放置在系统配置文件，修改参数放置在用户配置文件

## 配置方式

用配置文件可以管理多个远程服务器，其格式如下：

    Host 服务器名A
        user 用户名
        hostname 服务器ip
        port 端口号
        identityfile 本地私钥地址
        ...
    Host 服务器名B
        user 用户名
        hostname 服务器ip
        port 端口号
        identityfile 本地私钥地址
        ...
    ...
    ...
    Host *
        ...
        ...

通过`Host`指定配置块，用`tab`键来区分配置头和内置参数

所有参数值都可使用通配符设定，比如可以设置一个`Host`值为星号(`*`)，用于设置全局配置

注释用`#`号开头

**配置文件不区分大小写，所以`Host`和`host`一样**

## 常用配置选项

* 必须配置
    * `Host`：指定配置块
    * `User`：指定登录用户
    * `Hostname`：指定服务器地址，通常用`ip`地址
    * `Port`：指定端口号，默认值为`22`
* 可选
    * `Identityfile`：指定本地认证私钥地址
    * `ForwardAgent yes`：允许`ssh-agent`转发
    * `IdentitiesOnly`：指定`ssh`是否仅使用配置文件或命令行指定的私钥文件进行认证。值为`yes`或`no`，默认为`no`，该情况可在`ssh-agent`提供了太多的认证文件时使用
    * `IdentityFile`：指定认证私钥文件
    * `StrictHostKeyChecking`：有`3`种选项
        * `ask`：默认值，第一次连接陌生服务器时提示是否添加，同时如果远程服务器公钥改变时拒绝连接
        * `yes`：不会自动添加服务器公钥到`~/.ssh/known_hosts`中，同时如果远程服务器公钥改变时拒绝连接
        * `no`：自动增加新的主机键到`~/.ssh/known_hosts`中

## 使用方式

比如配置文件如下：

    Host server
        user ubuntu
        hostname 123.231.032.123
        port 22

连接方式如下：

    # 登录远程服务器
    $ ssh server
    # 传输文件
    $ scp hello.txt server:/home/ubuntu/

## 相关阅读

* [利用 SSH 的用户配置文件 Config 管理 SSH 会话](https://www.hi-linux.com/posts/14346.html)

* [SSH Config File](https://www.ssh.com/ssh/config/)
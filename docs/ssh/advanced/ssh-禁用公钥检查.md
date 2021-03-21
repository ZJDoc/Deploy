
# [SSH]禁用公钥检查

## 配置

第一次登录服务器时默认进行服务器公钥检查，可通过设置禁止

方法一：在`~/.ssh/config`文件中加入

    Host *
    StrictHostKeyChecking no
    # 或
    echo -e "Host ip-address\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config

方法二：在命令中添加禁止公钥检查参数

    $ ssh -o StrictHostKeyChecking=no ip-address

## 相关阅读

* [禁用SSH远程主机的公钥检查](http://www.worldhello.net/2010/04/08/1026.html)

* [TravisSendToServer](https://github.com/Godi13/TravisSendToServer/blob/master/.travis.yml)

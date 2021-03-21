
# 非root用户运行

默认安装的`tomcat`以`root`用户运行，为保证其安全性，进一步设置`tomcat`以普通用户运行

## 创建tomcat用户

创建新用户`tomcat`，设置`home`目录为`/opt/tomcat`

```
$ useradd -d /opt/tomcat tomcat
```

修改`/opt/tomcat`文件属主为`tomcat`

```
$ sudo chown -R tomcat:tomcat apache-tomcat-9.0.27
```

## 实现

切换到`tomcat`用户后进行启动即可；如果是开机自启动，则修改`/etc/rc.local`

```
su tomcat -c "/opt/apache-tomcat-9.0.27/bin/startup.sh"
```

这篇文章[How To Install Apache Tomcat 8 on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-8-on-ubuntu-16-04)也介绍的很详细

## 其他实现

`tomcat`提供了工具`jsvc`，允许`tomcat`以非`root`用户运行，参考[Unixroot daemon](https://tomcat.apache.org/tomcat-9.0-doc/setup.html)

## 相关阅读

* [用非root用户启动tomcat进程](https://rorschachchan.github.io/2018/04/18/%E4%BD%BF%E7%94%A8%E6%99%AE%E9%80%9A%E7%94%A8%E6%88%B7%E5%90%AF%E5%8A%A8tomcat/)

* [How To Install Apache Tomcat 8 on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-8-on-ubuntu-16-04)

* [Tomcat用普通用户身份运行](http://www.zhengdazhi.com/archives/1382)

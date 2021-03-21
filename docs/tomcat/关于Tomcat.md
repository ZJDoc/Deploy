
# 关于Tomcat

`Tomcat`文档在开头提供了一些重要的信息和内容 - [Introduction](https://tomcat.apache.org/tomcat-9.0-doc/introduction.html#CATALINA_HOME_and_CATALINA_BASE)

## 术语

具体规范参考：[Servlet and JSP specifications](https://wiki.apache.org/tomcat/Specifications)。比如

* `Context` - 表示一个`Web`应用程序

## 目录和文件

重要的`tomcat`目录：

1. `/bin`：启动、关闭以及其他一些脚本
2. `/conf`：配置文件和相关的`DTDs`，其中最重要的配置文件就是`server.xml`
3. `/logs`：默认放置的日志目录
4. `/webapps`：`webapp`存放的目录

## CATALINA_HOME和CATALINA_BASE

需要设置两个重要的环境变量：

1. `CATALINA_HOME`：表示`Tomcat`安装路径
2. `CATALINA_BASE`：表示特定`Tomcat`实例的运行时配置的根路径

默认情况下，两个环境变量设置为相同路径
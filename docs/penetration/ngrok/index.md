
# 引言

[Ngrok](https://github.com/inconshreveable/ngrok)是一个很有效的内网穿透工具，其不仅提供了在线服务，还可以自己搭建服务器进行内网穿透。首先介绍Ngrok进行内网穿透的具体实现，再进一步补充自建服务器的相关操作：

* [Ngrok实现内网穿透](./ngrok实现.md)
* [[ngrok]TCP和HTTP连接配置](./[ngrok]TCP和HTTP连接配置.md)：使用配置文件方式实现`HTTP`和`TCP`连接
* [[ngrok]Ubuntu service实现](./[ngrok]Ubuntu service实现.md)：配置`service`文件完成`ngrok`服务
* [[ngrok]docker实现](./[ngrok]docker实现.md)：使用`Docker`容器实现`ngrok`服务端
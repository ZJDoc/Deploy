
# [阿里云][域名解析]URL转发

## 需求描述

在远程服务器上使用`9980`端口实现`HTTPs`服务，直接访问方式如下：

```
https://www.test.com:9980
```

理想状态下是希望只输入域名而不需要额外端口号，解析后跳转到新地址并且能够指定端口，比如：

```
http://www.xxx.com  ->  https://www.test.com:9980
```

## URL转发

参考：

[添加网站解析](https://help.aliyun.com/document_detail/106535.html?spm=a2c4g.11186623.2.12.936e52fbvbu0gM)

[URL转发类问题排查](https://help.aliyun.com/knowledge_detail/118166.html)

阿里云域名解析服务提供了`URL转发`功能，能够实现`域名+端口`的绑定。实现如下：

1. 在记录类型中选择`显性URL`或者`隐性URL`
2. 记录值中可以输入域名+端口，比如`https://www.xxx.com:9980`

`显性URL`和`隐性URL`的区别在于`显性URL`服务会重定向到真实目标地址（也就是会在地址栏暴露端口号），而`隐形URL`服务会隐藏真实地址

**注意：`URL`转发前域名支持`HTTP`，不支持`HTTPS`，转发后的目标地址支持`HTTP、HTTPS`**
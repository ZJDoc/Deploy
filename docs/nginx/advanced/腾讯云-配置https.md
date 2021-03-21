
# [腾讯云]配置HTTPs

使用了腾讯云的`DNS`解析服务，顺便申请了`ssl`，其实现步骤和[[阿里云]配置HTTPs](./阿里云-配置https.md)没有差别，不过目前使用的`Nginx`版本更新，在具体配置上会有略微差别

**`Note`：当前`Nginx`版本为`nginx version: nginx/1.17.9`**

## CA证书

申请地址：[https://console.cloud.tencent.com/ssl](https://console.cloud.tencent.com/ssl)

一天内就可以完成审核，下载证书后将`nginx`部分放置在`/etc/nginx/ssl`文件夹中（这是我的配置，`/etc/nginx`是`nginx`配置文件路径，`ssl`是新建的文件夹）

## conf文件

在`/etc/nginx/conf.d`目录下新建配置文件`xxx.conf`

```
server {
     #SSL 访问端口号为 443
     listen 443 ssl; 
     #填写绑定证书的域名
     server_name xxx.xxx.xxx; 
     
     # 防止中文乱码
     charset utf-8;

     #证书文件名称
     ssl_certificate /etc/nginx/ssl/1_xxx.xxx.xxx_bundle.crt; 
     #私钥文件名称
     ssl_certificate_key /etc/nginx/ssl/2_xxx.xxx.xxx.key; 
     ssl_session_timeout 5m;
     #请按照以下协议配置
     ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 
     #请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
     ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
     ssl_prefer_server_ciphers on;

     location / {
        #网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
         #root /var/www/www.domain.com; 
        root   /opt/www; 
	    index  index.html index.htm;
     }

    error_page 404	/404.html;
 }
server {
	listen 80;
	#填写绑定证书的域名
	server_name xxx.xxx.xxx; 
	#把http的域名请求转成https
	return 301 https://$host$request_uri; 
}
```

>由于版本问题，配置文件可能存在不同的写法。例如：Nginx 版本为 nginx/1.15.0 以上请使用 listen 443 ssl 代替 listen 443 和 ssl on。

## 启动nginx

测试配置文件是否正确

```
$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

启动nginx

```
# 停止nginx
$ sudo systemctl stop nginx
# 启动nginx
$ sudo systemctl start nginx
# 查询nginx状态
$ sudo systemctl status nginx
```

## 相关阅读

* [Nginx 服务器证书安装](https://cloud.tencent.com/document/product/400/35244)
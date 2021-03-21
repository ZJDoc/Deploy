
# [译]NGINX Reverse Proxy

原文地址：[NGINX Reverse Proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)

>This article describes the basic configuration of a proxy server. You will learn how to pass a request from NGINX to proxied servers over different protocols, modify client request headers that are sent to the proxied server, and configure buffering of responses coming from the proxied servers.

本文描述了代理服务器的基本配置。您将学习如何通过不同的协议将请求从NGINX传递到目的服务器，修改发送到目的服务器的客户端请求头，以及配置来自目的服务器的响应的缓存

## 内容列表

>Table of Contents

>* Introduction
>* Passing a Request to a Proxied Server
>* Passing Request Headers
>* Configuring Buffers
>* Choosing an Outgoing IP Address

* 引用
* 将请求传递给目的服务器
* 传递请求头
* 配置缓存区
* 选择传出的IP地址

## 引言

>Introduction

>Proxying is typically used to distribute the load among several servers, seamlessly show content from different websites, or pass requests for processing to application servers over protocols other than HTTP.

代理通常用于在几个服务器之间分配负载，无缝显示来自不同网站的内容，或者通过不同于HTTP的协议将处理请求传递给应用服务器

## 将请求传递给目的服务器

>Passing a Request to a Proxied Server

>When NGINX proxies a request, it sends the request to a specified proxied server, fetches the response, and sends it back to the client. It is possible to proxy requests to an HTTP server (another NGINX server or any other server) or a non-HTTP server (which can run an application developed with a specific framework, such as PHP or Python) using a specified protocol. Supported protocols include `FastCGI, uwsgi, SCGI, and memcached`.

当NGINX代理一个请求时，它将该请求发送到指定的目的服务器，获取响应，并将其发送回客户端。可以使用指定的协议将请求代理到一个HTTP服务器(另一个NGINX服务器或任何其他服务器)或非HTTP服务器(可以运行用特定框架开发的应用程序，如PHP或Python)。支持的协议包括[FastCGI](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html?_ga=2.211916566.387393077.1583909280-1052863427.1583909280)、[uwsgi](https://nginx.org/en/docs/http/ngx_http_uwsgi_module.html?_ga=2.211916566.387393077.1583909280-1052863427.1583909280)、[SCGI](https://nginx.org/en/docs/http/ngx_http_scgi_module.html?_ga=2.211916566.387393077.1583909280-1052863427.1583909280)和[memcached](https://nginx.org/en/docs/http/ngx_http_memcached_module.html?_ga=2.179983398.387393077.1583909280-1052863427.1583909280)

>To pass a request to an HTTP proxied server, the `proxy_pass` directive is specified inside a `location`. For example:

为了将请求传递给一个HTTP目的服务器，[proxy_pass](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.179983398.387393077.1583909280-1052863427.1583909280#proxy_pass)指令是在一个[location](https://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=2.179983398.387393077.1583909280-1052863427.1583909280#location)内指定的。例如:

```
location /some/path/ {
    proxy_pass http://www.example.com/link/;
}
```

>This example configuration results in passing all requests processed in this location to the proxied server at the specified address. This address can be specified as a domain name or an IP address. The address may also include a port:

这个示例配置将符合这个location处理的所有请求传递到指定地址。该地址可以指定为域名或IP地址。该地址还可以包括一个端口号:

```
location ~ \.php {
    proxy_pass http://127.0.0.1:8000;
}
```

>Note that in the first example above, the address of the proxied server is followed by a URI, `/link/`. If the URI is specified along with the address, it replaces the part of the request URI that matches the location parameter. For example, here the request with the `/some/path/page.html` URI will be proxied to `http://www.example.com/link/page.html`. If the address is specified without a URI, or it is not possible to determine the part of URI to be replaced, the full request URI is passed (possibly, modified).

请注意，在上面的第一个示例中，目的服务器的地址后跟一个URI，`/link/`。如果URI与地址一起指定，它将替换请求中与location参数匹配的URI部分。例如，此处带有`/some/path/page.html `URI的请求将被代理到`http://www.example.com/link/page.html`。如果指定的地址没有URI，或者无法确定要替换的URI部分，则完整的请求URI将被传递(可能被修改)

>To pass a request to a non-HTTP proxied server, the appropriate `**_pass` directive should be used:
>* `fastcgi_pass` passes a request to a FastCGI server
>* `uwsgi_pass` passes a request to a uwsgi server
>* `scgi_pass` passes a request to an SCGI server
>* `memcached_pass` passes a request to a memcached server

要将请求传递给非HTTP目的服务器，应该使用适当的`**_pass`指令:

* `fastcgi_pass`将请求传递给FastCGI服务器
* `uwsgi_pass`将请求传递给uwsgi服务器
* `scgi_pass`将请求转递给SCGI服务器
* `memcached_pass`将请求传递给memcached服务器

>Note that in these cases, the rules for specifying addresses may be different. You may also need to pass additional parameters to the server (see the `reference documentation` for more detail).

请注意，在这些情况下，指定地址的规则可能不同。您可能还需要向服务器传递额外的参数(有关更多详细信息，请参见[参考文档](https://nginx.org/en/docs/?_ga=2.187269034.387393077.1583909280-1052863427.1583909280))

>The `proxy_pass` directive can also point to a `named group` of servers. In this case, requests are distributed among the servers in the group according to the specified method.

[proxy_pass](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.183054500.387393077.1583909280-1052863427.1583909280#proxy_pass)指令还可以指向一组服务器的[命名组](https://nginx.org/en/docs/http/load_balancing.html?&_ga=2.183054500.387393077.1583909280-1052863427.1583909280#algorithms)。在这种情况下，请求根据指定的方法分布在组中的服务器之间

## 传递请求头

>Passing Request Headers

>By default, NGINX redefines two header fields in proxied requests, `Host` and `Connection`, and eliminates the header fields whose values are empty strings. `Host` is set to the `$proxy_host` variable, and `Connection` is set to `close`.

默认情况下，NGINX在代理请求中重新定义了两个头字段，`Host`和`Connection`，并删除了值为空字符串的头字段。`Host`设置为`$proxy_host`变量，`Connection`设置为`close`

>To change these setting, as well as modify other header fields, use the `proxy_set_header` directive. This directive can be specified in a `location` or higher. It can also be specified in a particular `server` context or in the `http` block. For example:

要更改这些设置以及修改其他标题字段，请使用[proxy_set_header](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.23288888.387393077.1583909280-1052863427.1583909280#proxy_set_header)指令。该指令可以在一个`location`或更高的[location](https://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=2.220363546.387393077.1583909280-1052863427.1583909280#location)中指定。它也可以在特定的[服务器](https://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=2.220363546.387393077.1583909280-1052863427.1583909280#server)上下文或[http](https://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=2.220363546.387393077.1583909280-1052863427.1583909280#http)块中指定。例如:

```
location /some/path/ {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_pass http://localhost:8000;
}
```

>In this configuration the `Host` field is set to the `$host` variable.

在此配置中，`Host`字段被设置为[$host](https://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=2.216112148.387393077.1583909280-1052863427.1583909280#variables)变量

>To prevent a `header` field from being passed to the proxied server, set it to an empty string as follows:

为了防止`header`字段传递给目的服务器，请将其设置为空字符串，如下所示:

```
location /some/path/ {
    proxy_set_header Accept-Encoding "";
    proxy_pass http://localhost:8000;
}
```

## 配置缓存区

>Configuring Buffers

>By default NGINX buffers responses from proxied servers. A response is stored in the internal buffers and is not sent to the client until the whole response is received. Buffering helps to optimize performance with slow clients, which can waste proxied server time if the response is passed from NGINX to the client synchronously. However, when buffering is enabled NGINX allows the proxied server to process responses quickly, while NGINX stores the responses for as much time as the clients need to download them.

默认情况下，NGINX缓存来自目的服务器的响应。响应存储在内部缓存区中，在收到整个响应之前不会发送给客户端。缓存有助于优化慢速客户端的性能，如果响应从NGINX同步传递到客户端，这会浪费目的服务器时间。但是，当启用缓存时，NGINX允许目的服务器快速处理响应，而NGINX存储响应的时间与客户端下载响应的时间一样长

>The directive that is responsible for enabling and disabling buffering is `proxy_buffering`. By default it is set to on and buffering is enabled.

负责启用和禁用缓存的指令是[proxy_buffering](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.20617402.387393077.1583909280-1052863427.1583909280#proxy_buffering)。默认情况下，它设置为on，表示启用缓存操作

>The `proxy_buffers` directive controls the size and the number of buffers allocated for a request. The first part of the response from a proxied server is stored in a separate buffer, the size of which is set with the `proxy_buffer_size` directive. This part usually contains a comparatively small response header and can be made smaller than the buffers for the rest of the response.

[proxy_buffers](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.258235528.387393077.1583909280-1052863427.1583909280#proxy_buffers)指令控制了为`请求`分配的缓存区的大小和数量。来自目的服务器的响应的第一部分存储在单独的缓存区中，缓存区的大小由[proxy_buffer_size](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.220960666.387393077.1583909280-1052863427.1583909280#proxy_buffer_size)指令设置。这部分通常包含一个相对较小的响应头，并且可以比其余响应的缓存区小

>In the following example, the default number of buffers is increased and the size of the buffer for the first portion of the response is made smaller than the default.

在下面的示例中，默认缓存区数量增加，并且响应第一部分的缓存区大小小于默认值

```
location /some/path/ {
    proxy_buffers 16 4k;
    proxy_buffer_size 2k;
    proxy_pass http://localhost:8000;
}
```

>If buffering is disabled, the response is sent to the client synchronously while it is receiving it from the proxied server. This behavior may be desirable for fast interactive clients that need to start receiving the response as soon as possible.

如果缓存被禁用，则当代理服务器从目的服务器接收响应时，该响应被同步发送到客户端。对于需要尽快开始接收响应的快速交互客户端，这种行为可能是理想的

>To disable buffering in a specific location, place the `proxy_buffering` directive in the `location` with the off parameter, as follows:

要禁用特定location的缓冲，在[location](https://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=2.255565706.387393077.1583909280-1052863427.1583909280#location)中设置[proxy_buffering](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.255565706.387393077.1583909280-1052863427.1583909280#proxy_buffering)指令为off，如下所示:

```
location /some/path/ {
    proxy_buffering off;
    proxy_pass http://localhost:8000;
}
```

>In this case NGINX uses only the buffer configured by `proxy_buffer_size` to store the current part of a response.

在这种情况下，NGINX只使用[proxy_buffer_size](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.218929179.387393077.1583909280-1052863427.1583909280#proxy_buffer_size)配置的缓冲区来存储响应的当前部分

>A common use of a reverse proxy is to provide load balancing. Learn how to improve power, performance, and focus on your apps with rapid deployment in the free `Five Reasons to Choose a Software Load Balancer` ebook.

反向代理的一个常见用途是提供负载平衡。在免费的[《选择软件负载平衡器的五个理由》](https://www.nginx.com/resources/library/five-reasons-choose-software-load-balancer/?_ga=2.218929179.387393077.1583909280-1052863427.1583909280 )电子书中，了解如何通过快速部署来提高能力、性能和专注于您的应用

## 选择传出的IP地址

>Choosing an Outgoing IP Address

>If your proxy server has several network interfaces, sometimes you might need to choose a particular source IP address for connecting to a proxied server or an upstream. This may be useful if a proxied server behind NGINX is configured to accept connections from particular IP networks or IP address ranges

如果您的代理服务器有多个网络接口，有时您可能需要选择一个特定的源IP地址来连接到目的服务器或上游。如果NGINX后面的目的服务器被配置为接受来自特定IP网络或IP地址范围的连接，这可能会很有用

>Specify the `proxy_bind` directive and the IP address of the necessary network interface:

指定[proxy_bind](https://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=2.259292040.387393077.1583909280-1052863427.1583909280#proxy_bind)指令和必要网络接口的IP地址:

```
location /app1/ {
    proxy_bind 127.0.0.1;
    proxy_pass http://example.com/app1/;
}

location /app2/ {
    proxy_bind 127.0.0.2;
    proxy_pass http://example.com/app2/;
}
```

>The IP address can be also specified with a variable. For example, the `$server_addr` variable passes the IP address of the network interface that accepted the request:

IP地址也可以用变量来指定。例如，[$server_addr](https://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=2.216626068.387393077.1583909280-1052863427.1583909280#var_server_addr)变量传递接受请求的网络接口的IP地址:

```
location /app3/ {
    proxy_bind $server_addr;
    proxy_pass http://example.com/app3/;
}
```
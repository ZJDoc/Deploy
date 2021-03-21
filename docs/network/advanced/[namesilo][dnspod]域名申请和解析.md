
# [namesilo][dnspod]域名申请和解析

之前在大陆地址申请了域名，并搭建了一个博客网站。前几天腾讯云客户通知我整改博客中存在外部链接的问题，因为不想要做任何限制，所以打算在香港申请服务器进行网站搭建，顺便也在国外注册了一个域名

## 域名选择

参考[有哪些国外便宜域名注册商是值得推荐的？](https://zhuanlan.zhihu.com/p/63866401)，在[namesilo](https://www.namesilo.com/)上注册域名

## namesilo域名申请

参考[Namesilo 域名购买保姆式教程，赠送1刀优惠码！](https://zhuanlan.zhihu.com/p/82666679)，注册完成用户后，选择自己喜欢的域名，购买即可

## dnspod域名解析

`namesilo`自带了域名解析服务，但是还是选择了国内的域名解析厂商[DNSPod](https://www.dnspod.cn)。参考[免费namesilo域名注册解析到dnspod教程](https://since1989.org/stuff/dnspod-name-servers-domain.html)，首先在`namesilo`中修改`nameserver`，添加`DNSPod`地址

```
f1g1ns1.dnspod.net
f1g1ns2.dnspod.net
```

然后在`DNSPod`上注册账户，添加域名

**注意：上述两个过程都需要几个小时的解析，耐性等待即可**

最后在`DNSPod`上添加解析记录，将域名和服务器`IP`绑定
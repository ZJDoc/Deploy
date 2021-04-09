
# 宝塔面板部署

## 安装

```
bash deploy.sh
```

## 登录方式

* 登陆地址 http://{{面板ip地址}}:8888

* 初始账号 username

* 初始密码 password

## 用户名/密码出错

参考[初始的用户名密码登陆错误 #66 ](https://github.com/pch18-docker/baota/issues/66)

```
同密码错误
解决方法：
docker exec -it baota bash
进入宝塔的docker容器内部
输入bt选择5和6修改账号密码
ctrl+d退出容器且保持容器运行
```

## 相关阅读

*  [宝塔面板一键docker部署](https://hub.docker.com/r/pch18/baota)
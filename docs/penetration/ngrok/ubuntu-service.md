
# Ubuntu Service实现

分别在服务器和客户端配置`ngrok service`服务

## 服务端

在`/opt/ngrok`目录内存放应用`ngrokd`及配置文件

```
├── a.key
├── a.pem
├── ngrokd
└── ngrokd.sh
```

其中`ngrokd.sh`是脚本内容，用于启动`ngrokd`

```
#!/bin/bash

cd /opt/ngrokd
./ngrokd -tlsKey=a.key -tlsCrt=a.pem -domain="xxx.xxx.xxx" -httpAddr=":xxxx" -httpsAddr=":xxxx" -tunnelAddr=":xxxx"
```

在`/etc/systemd/system/`目录内编写`ngrokd.service`文件

```
[Unit]
Description= Ngrok
Documentation=https://github.com/inconshreveable/ngrok

[Service]
ExecStart=/bin/bash /opt/ngrokd/ngrokd.sh
Type=simple
KillMode=process
Restart=no
RestartSec=42s

[Install]
WantedBy=multi-user.target
```

## 客户端

在`/opt/ngrok`目录内存放应用`ngrok`及配置文件

```
├── ngrok
├── ngrok.cfg
└── ngrok.sh
```

其中`ngrok.sh`是脚本内容，用于启动`ngrok`

```
#!/bin/bash

cd /opt/ngrok
./ngrok -config ngrok.cfg start-all
```

在`/etc/systemd/system/`目录内编写`ngrok.service`文件

```
[Unit]
Description= Ngrok
Documentation=https://github.com/inconshreveable/ngrok

[Service]
ExecStart=/bin/bash /opt/ngrokd/ngrok.sh
Type=simple
KillMode=process
Restart=no
RestartSec=42s

[Install]
WantedBy=multi-user.target
```

## 使用

```
# 重载service配置
$ sudo systemctl daemon-reload
# 启动
$ sudo systemctl start ngrokd.service
# 开机子启动
$ sudo systemctl enable ngrokd.service
```
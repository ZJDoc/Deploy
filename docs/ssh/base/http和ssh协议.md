
# http和ssh协议

大多数`git`托管网站都支持使用`http`协议或`ssh`协议进行代码拉取和推送操作

## `http`

其命名方式如下：

    https://<website-name>/<user-name>/<repo-name>.git

    # github仓库
    https://github.com/zjZSTU/zjzstu.github.com.git
    # gitee仓库
    https://gitee.com/zjZSTU/zjzstu.gitee.io.git

使用`http`协议的优点在于每次推送都需要进行授权验证，服务器会提示你输入用户名和密码

## `ssh`

其命名方式如下：

    git@<website-name>:<user-name>/<repo-name>.git

    # github仓库
    git@github.com:zjZSTU/zjzstu.github.com.git
    # gitee仓库
    git@gitee.com:zjZSTU/zjzstu.gitee.io.git

使用`ssh`协议进行代码推送之前需要进行`ssh`密钥认证，在本地生成`ssh`密钥，上传`ssh`公钥到托管网站，这样每次推送就能自动认证

## 相关阅读

* [4.1 服务器上的 Git - 协议](https://git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E5%8D%8F%E8%AE%AE)
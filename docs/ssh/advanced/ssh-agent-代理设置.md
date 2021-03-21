
# [ssh-agent]代理设置

## 配置

生成新的`ssh`密钥之后，可以添加私钥到`ssh-agent`，这样之后拉取新的仓库或测试时就不再需要输入密码了

1. 启动`ssh-agent`

        $ eval "$(ssh-agent -s)"
        Agent pid 7804

2. 添加`ssh`私钥

        $ ssh-add ~/.ssh/xxx_id_rsa
        Enter passphrase for /home/zj/.ssh/github_id_rsa: 
        Identity added: /home/zj/.ssh/github_id_rsa (/home/zj/.ssh/github_id_rsa)

## 相关阅读

* [Adding your SSH key to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#adding-your-ssh-key-to-the-ssh-agent)
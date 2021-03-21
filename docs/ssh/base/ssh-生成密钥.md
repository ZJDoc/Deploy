
# [SSH]生成密钥

## 查询

验证本地是否已存在密钥

    $ cd ~/.ssh/

查看是否存在`id_dsa`或`id_rsa`命名的文件，其中`.pub`文件是公钥

## 生成

在本地生成密钥，使用`ssh-keygen`进行，默认生成`id_rsa`文件在`~/.ssh`文件夹内

    $ ssh-keygen 
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/zj/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /home/zj/.ssh/id_rsa.
    Your public key has been saved in /home/zj/.ssh/id_rsa.pub.
    The key fingerprint is:
    ...
    ...

其中会要求你输入两次密码，也可以为空

    $ ls
    id_rsa  id_rsa.pub  ...

### 自定义

指定密钥加密算法、密钥长度、密钥标签、密钥文件名

    $ ssh-keygen -t rsa -b 4096 -C "github.com" -f ~/.ssh/github_id_rsa
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /home/zj/.ssh/github_id_rsa.
    Your public key has been saved in /home/zj/.ssh/github_id_rsa.pub.
    The key fingerprint is:
    SHA256:WRZktNSVoY+a5hAgNwou
    ...
    ...

* `-t`指定加密算法，当前设置为`rsa`加密算法
* `-b`指定密钥长度
* `-C`指定了标签
* `-f`指定生成文件名

当你已经存在`github_id_rsa/github_id_rsa.pub`文件时，会提示你是否重载

## 重设密钥

重新设置密钥密码

    $ ssh-keygen -p
    Enter file in which the key is (/home/zj/.ssh/id_rsa):  # 默认是id_rsa文件，点击Enter键；否则，输入正确文件地址
    Enter old passphrase:                                   # 输入旧密码
    Enter new passphrase (empty for no passphrase):         # 输入新密码
    Enter same passphrase again:                            # 重复新密码
    Your identification has been saved with the new passphrase.

或者加上参数`-f`指定要修改的文件

    $ ssh-keygen -p -f /home/zj/.ssh/github_id_rsa
    Enter old passphrase: 
    Enter new passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved with the new passphrase.

或者加上参数`-P`指定旧密码、`-N`指定新密码

    $ ssh-keygen -p -P zhujian -N 123456 -f ~/.ssh/github_id_rsa
    Your identification has been saved with the new passphrase.

## 相关阅读

* [4.3 服务器上的 Git - 生成 SSH 公钥](https://git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E7%94%9F%E6%88%90-SSH-%E5%85%AC%E9%92%A5)
* [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
* [Working with SSH key passphrases](https://help.github.com/articles/working-with-ssh-key-passphrases/)
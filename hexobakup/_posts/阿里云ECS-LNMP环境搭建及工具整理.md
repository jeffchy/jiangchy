---
title: 阿里云ECS LNMP环境搭建及工具整理
date: 2017-01-20 23:28:57
tags:
- Web
- Aliyun
- CentOS
- LNMP
categories:
- Tech
- Note
---
今天我又给阿里云掏腰包了，由于最近稍微了解了一些python的Web框架，但是折腾个来去发现自己无法在原来有的云虚拟主机上面部署（需要python+django+tools的环境，而云虚拟主机里面的环境是死的，很多时候很不方便），于是我没忍住就剁手了，买了一个月的阿里云ECS云服务器试一试，并且折腾了好一阵子完成了ECS上LNMP环境的搭建，完成了一个静态站点的迁移。
<!-- more -->
### 关于ECS
对于一个小规模的个人网站来说（或者APP），1G的内存，1M带宽，1个核心，40G的高效云盘就完全够用了，我用的操作系统是**CentOS7.2**，因为CentOS是目前服务器使用最广泛的Linux发行版。

## 获得LNMP的最简单方法
如果你购买阿里云的ECS，现在可以选择购买镜像，这里的镜像就是指一套成熟的环境安装包，并配上说明文档和安装脚本等等，基本上都免费，所以最简单的方法当然是在购买的时候选择获取这种第三方镜像。
![在ECS的购买页面点击选择市场镜像](/images/image/ECS/1.png)
选择符合要求的镜像+操作系统的服务器。
这应该是最简单的方法了，适合linux萌新，但不是我用的方法，为什么我不用呢？主要想折腾一下锻炼一下自己(划掉 其实就是不知道这茬而已)，不过说真的，学到不少。

## 如何远程连接ECS服务器？
方法有很多种，**强烈推荐使用最新你的Xshell5**，对于家庭和学生免费，[官网连接](http://www.netsarang.com/products/xsh_overview.html)
新建站点，输入用户密码之类的就能够远程连接CentOS服务器了，而且效果很不错，远远好于阿里云自带的远程连接工具。效果如图。
![效果如图](/images/image/ECS/2.PNG)
[Xshell链接ECS教程](http://jingyan.baidu.com/article/75ab0bcbc40b39d6864db23c.html)

## 如何与服务器之间进行文件传输交互？
笔者现在用的FlashFXP 5，体验非常不错，但是需要付费，有免费三十天的试用期，我们不必配置一堆ftp的内容，我们可以在**设置完防火墙之后**，使用SFTP SSH的方式远程连接。
[教程-百度经验](http://jingyan.baidu.com/article/a24b33cd77a0dc19fe002bae.html)
**ATTENTION:** 在配置防火墙的时候可能会出现错误，原因是CentOS7.2的默认防火墙不在是iptables而被换成了firewall,所以我们有两种办法，第一种是将firewall的服务禁用掉，并且安装并且启用iptables的服务，第二种也很简单，直接让firewall支持开放服务器的端口，笔者采用的是第一种方法。具体教程，看着[这篇文章](http://blog.csdn.net/u012456926/article/details/50096473)

### 如何配置LNMP环境？
## 什么是LNMP?
LNMP = Linux + Nginx + MySQL(mariaDB) + php

安装环境：CentOS7.2
## Nginx
可直接用yum包管理器安装
`yum install nginx`
安装完毕之后启用服务，需要**已经按照上文的教程配置防火墙**
`systemctl start nginx`
之后我们可以在浏览器中输入
`<服务器外网ip>`
如果出现nginx的默认页面，说明安装成功
之后我们将nginx设置为开机自启动
`systemctl enable nginx.service`

## MySQL/MariaDB
同样之间yum安装mariadb
`yum install mariadb-server`

启用mariadb服务
`systemctl start mariadb`

对mariadb进行配置
`/usr/bin/mysql_secure_installation`

之后mariadb会让你输密码，以及会问一系列问题，根据你的情况直接选择Y/N，可以直接按照默认来设置，设置完成之后会看到success

将mariadb设置成开机自启动
`systemctl enable mariadb`

## 安装php及所需工具
yum安装及启动php-fpm
`yum install php-fpm php-mysql`
`systemctl start php-fpm`
`systemctl enable php-fpm`

设置一下php session的目录
`mkdir /var/lib/php/session/`
`chown -R apache:apache /var/lib/php/session/`

配置nginx
首先找到nginx的配置文件。注意！每个nginx版本他的配置文件地点不一样，nginx的默认页面会告诉你他的配置文件在哪里。一般叫做nginx.conf

在修改之前先进行备份
`cp nginx.conf nginx.conf.bak`

用vi将nginx.conf文件进行修改，在其中加入如下代码
```
location ~ \.php$ {
        root           /usr/share/php; # 你存放php脚本的地方
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }
```

如果不知道如何配置，或者想要自定义的话，可以打开**nginx.conf.default**一探究竟，里面有官方的注释

好大概就是这样，中途免不了更多折腾和问题，如果有就请教度娘谷歌吧

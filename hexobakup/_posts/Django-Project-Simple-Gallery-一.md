---
title: 'Django Project: Simple Gallery(二)'
date: 2017-02-01 21:01:08
tags:
- Web
- python
- Django
categories:
- Tech
- Note
---
大家好久不见，我把gallery部署了，不过先没有部署在阿里云上，而是在pythonanywhere上，说一下如何在上面部署吧。
链接：[http://jeffchiang.pythonanywhere.com/gallery/](http://jeffchiang.pythonanywhere.com/gallery/)
<!-- more -->
[官方文档：如何在pythonanywhere上部署已经有的django项目](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject)
首先先注册，然后登录。
如果你不需要什么额外的虚拟环境，点击WEB选项卡，然后创建新的app，选择你用的django版本，python版本，project名称啥的。
创建好了以后，打开console的bash，用git克隆你的代码到响应文件夹下(当然也可以直接在网页上操作不过比较慢)，如果你正确地把文件归位，把static、templates、media的url都设置正确，那么可以直接reload，直接访问网址，就可以啦。

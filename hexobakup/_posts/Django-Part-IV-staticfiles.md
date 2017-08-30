---
title: Django Part IV staticfiles
date: 2017-01-23 18:38:20
tags:
- Web
- python
- Django
categories:
- Tech
- Note
---
Django 1.10.5 + python 3.5.3
简要总结一下如何设置static files，如图片，CSS，JS

首先,[官方文档](https://docs.djangoproject.com/en/1.10/howto/static-files/)比较权威 
总结几点：
* 在app的subdir中创建folder：static,确保static和templates在同一个目录下
* 自动生成的project和app中已经将**django.contrib.staticfiles**加入settings.py中的INSTALLED_APPS,如果因为一些原因没有添加，补上
* 同样，应该已经有`STATIC_URL = '/static/'`在settings.py中。
* 在你的templates文件中确保做到两件事，第一，在文件头部加入load static，自动脑补花括号和百分号
* `src=" static "images/example.jpg" `自动脑补花括号和百分号，hexo禁止提交这些字符

官方文档中有其他功能，如自行指定不在app中的static路径等等，祝好。

官方文档的坑真的好多啊啊啊啊啊！
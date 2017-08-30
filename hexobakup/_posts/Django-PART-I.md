---
title: Django PART I
date: 2017-01-17 20:58:46
tags:
- Web
- python
- Django
categories:
- Tech
- Note
---
这几天我把django的官方文档的入门部分看了一遍，略有所悟，是时候写一点东西总结一下了。
<!-- more -->
### MVC
MVC全名是Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。MVC被独特的发展起来用于映射传统的输入、处理和输出功能在一个逻辑的图形化用户界面的结构中。(引自百度百科)
### Django
Django是一个开放源代码的Web应用框架，由Python写成。Django是一个基于MVC构造的框架。但是在Django中，控制器接受用户输入的部分由框架自行处理，所以 Django 里更关注的是模型（Model）、模板(Template)和视图（Views），即MTV模式
## 重要命令
`django-admin startproject projectname` 创建project
```
mysite/ 目录结构
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
`python manage.py runserver` 运行python内置开发服务器
`python manage.py startapp appname` 创建一个web app
```
appname/ 子目录结构
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

大致的工作流是怎么样的呢？
* view是url响应的结果，所以我们编写了一个view视图，就需要有一个url与之对应，写在urlpattern中，构建一个url类的实例，具体初始化参数至少包括，一个正则表达式（regex）用来匹配url，一个对应的视图，一个name，给url取个名字，方便在别的地方引用，这样如果urlpattern被修改，别的地方不用修改
* 一个project中可以涵盖多个app,新建了一个app的view，需要在app目录下的url进行一遍config。
* 同样的我们别忘了在app的父级，也就是project中的url.py中进行一个config,具体办法是用include()方法，将app中的url“导入”进来
* setup数据库,`python manage.py migrate`
* 创建数据模型(models.py),每个模型都继承于django.db.models.Model的类，类之中需要设置在数据库中存储的空间类型如**Field**以及关系如**ForeignKey**
* 在设置setting.py中的INSTALLED_APPS中加上我们新创建的appname `'appname.apps.AppnameConfig'`,说明我们已经install了这个app
* `python manage.py makemigrations polls` 将这些数据模型的变化转换为数据库中数据的“迁移”。
* `python manage.py migrate` 应用“迁移”(migrate),数据库中的数据模型响应命令，发生变更。
* 改变数据模型的子工作流：models.py*->makemigrations->migrate
* Django有关于database的[API](https://docs.djangoproject.com/en/1.10/topics/db/queries/),可以用python对数据库中的数据进行各种操作。
* 建好数据模型后，用admin-site来直接操作数据库。
* 那么templates是用来做什么的呢？**View**中可以通过调用（load)templates来将template中定制的内容在结合model中的底层数据行程一个context，最终提交一个templates和一个context行程HttpResponse，反馈给浏览器，真正的view也就形成了

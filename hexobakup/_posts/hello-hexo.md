---
title: Hello Hexo
date: 2016-12-02 18:20:21
tags:
- Hexo
- Web
categories:
- Tech
---
## 这是一个大二学生的个人博客。
我会陆续更新和分享我学zhe习teng过程中的一些心得体会[smirk]。

一直有搭博客的想法，真正写过一点前端代码的人才懂写前端真的是一个要花很多时间和体力的活计。
而要搭一个博客，不仅要好看，还要进行反复的管理，学校的课业太辛苦了，没这个时间也没这个精力，也没这个技术。
### So, hello hexo.
没想到搭博客这么简单[smirk]。
<!--more-->
首先分享一下我觉得不错的两个小白教程，顺便学习一下Markdown。
[百度经验](http://jingyan.baidu.com/article/d8072ac47aca0fec95cefd2d.html)   [tuicool](http://www.tuicool.com/articles/ueI7naV)
这两篇基本上能解决大部分问题了。

## 简要的梳理一下吧
### 为什么用Hexo
  对我个人来说，就两个原因。
  * 我目前的开发环境是 windows 10，相比另一个主流工具 jekyll，Hexo只需要依赖Node.js,安装非常方便。虽然我有Ubuntu双系统，但我懒得去配置一堆jekyll所需要的Ruby环境了。
  * 高颜值，没谁了。
### 配置的简要步骤
  * 官网下载[Node.js](nodejs.cn)
  * 如果你在windows下，你需要Git Bash和Github账号(optional)
  * 在一个你喜欢的地方新建文件夹，如 /BLOG
  * 进入BLOG文件夹，打开Git Bash
### 我们来敲命令吧！

全局安装hexo
`npm install -g hexo `  

初始化hexo以及安装剩余依赖
`hexo init`
`npm install`   

用hexo生成静态页面
`hexo generate`   

用浏览器预览你的页面，运行命令后浏览器打开 http://localhost:4000/
`hexo server`   

如果你发现死活打不开，可能是由于端口4000被占用，你可以打开任务管理器确认一下，可以用如下命令解决问题:
`hexo server -p 3999`   

你还需要安装一个发布到github的工具    
`npm install hexo-deployer-git`  

修改目录下的_config.yml以发布到你的github(optional)
        # Deployment
        ## Docs: http://hexo.io/docs/deployment.html
        deploy:
        type: git
        repo: https://github.com/your-site-repo-in-githubbalabala
        branch: master
最后一步
`hexo deploy`
你会发现你的远成仓库满当当的，enjoy

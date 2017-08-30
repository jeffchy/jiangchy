---
title: MySQL 安装及配置 MOOC笔记(一)
date: 2017-01-13 21:15:38
tags:
- Web
- Database
- MySQL
categories:
- Tech
- Note
---
今天进行了一下数据库的配置，使用版本：MySQL5.7.17 Community 操作系统：Win10 x64
顺便稍微用MOOC入门一下MySQL数据库，总要用到。课程链接[http://www.imooc.com/learn/122](http://www.imooc.com/learn/122)
<!--more-->
## 安装及配置
[安装及配置参考链接，转载，实测可用](http://www.cnblogs.com/huixing/p/6122488.html)
Tips:
* 需要用**管理员权限**打开CMD
* 上文中的';'不要忘记，为必须
* 按部就班即可

## 规范
* 关键字、函数名uppercase
* 数据库名、表名、字段名lowercase
* SQL语句分好结尾
## 常用命令（一） 
* 开启服务：CMD中 net start mysql
* 停止服务：CMD中 net stop mysql
* root登录数据库： mysql -u root -p 接着输入密码
* 登陆后退出： quit

## 常用命令（二）
* 修改命令提示符： mysql -u root -p 密码 --prompt 提示符（\D \d \h \u...）
* 显示版本： SELECT VERSION();
* 显示当前日期： SELECT NOW();
* 显示当前用户： SELECT USER();

## 常用命令（三）
* 创建数据库：CREATE DATABASE name
* 显示数据库：SHOW DATABASES;
* 修改数据库：ALTER DATABASE name CHARACTER SET utf8;
* 删除数据库：DROP DATABASE name;

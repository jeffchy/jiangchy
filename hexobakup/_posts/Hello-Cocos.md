---
title: Hello Cocos (i)OverView
date: 2016-12-03 12:16:34
tags:
- CocosCreator
- Web
- Js
- Game
categories:
- Tech
---
## 这是一个大二学生用一个月挤出的课余时间给女友写的生日礼物
[My Game your Game](http://xuyiwenzhuzhuzhu.cn/game.html)
[Github Source Code](https://github.com/jeffchy/projectzhuzhuzhu-Cocoscreator)
所用开发工具：CocosCreator、VScode、Chrome、PS、AU
这不是一个教你如何一步一步写出我这样的一个游戏的教程，因为代码挺多的，说不完，我会分享一下写这个项目的时候总结的一些心得体会，以及这个2D游戏引擎常用的一些关键操作。

所以我们开始吧:)
<!--more-->

### 为什么选择CocosCreator
[CocosCreator](http://www.cocos.com/)是一个很不错的2D游戏开发引擎，虽然是一个2016年的新工具，但是它也是从Cocos2d-x、CocosStudio一步一步进化而来。
之前有用过C++写过一点点Cocos2d-x,但是写完了场景跳转就感觉写不下去了，而CocosCreator的好处就是脚本驱动，将游戏开发脚本化模块化了，不仅更加贴近于Unity3D的模式,而且门槛降低了很多，还有很关键的一点，他将UI设计、Anim制作、Coding集成在同一个平台上，但是互相之间也有明确的界限，是的开发者和设计者可以相互合作，提高效率。哦对了，可以比较方便地发布到各个平台（WebDesktop WebMobile Android IOS Win32 OSX），很强。

### 为什么想到要写个游戏
不为什么，就想找个project开发开发，开发啥不重要，主要两个目的：
* 告诉女友 I love her
* 锻炼一下自己，因为平时虽然也会经常有几百行代码的作业，但和开发的思路还是不太一样的。

*** 
我试一试Markdown的分割线 
### 我写了个啥？
如果你玩过上面的链接，你应该就懂了，一个游戏逻辑十分简单，但是尽可能加了一些功能和变化提高可玩性和颜值的游戏。
![](/images/image/HelloCocos1/1.png)
这是工作界面，里面主要由层级管理器、资源管理器、场景编辑器、控件库、属性检查器、控制台、动画编辑器组成。
这些基本但是重要的东西，还是看[官方文档](http://www.cocos.com/docs/creator/getting-started/index.html)最好。
看完应该就有一个一知半解了。在仔细一点地分析这个游戏之前，我把我的学习路线分享给大家。

### 小白如何学习CocosCreator？
* 看完[官方文档](http://www.cocos.com/docs/creator/getting-started/index.html)的入门部分。
* 认真敲完官方文档中的[实例游戏](http://www.cocos.com/docs/creator/getting-started/quick-start.html)，这就是我游戏的原型[smirk]。
* 同时非常建议提前看一下另外两个实例游戏的代码。[DuangSheep](https://github.com/cocos-creator/tutorial-duang-sheep),[暗黑斩](https://github.com/cocos-creator/tutorial-dark-slash)，以及官方的[范例集合](https://github.com/cocos-creator/example-cases)。
* 敲完以后认真想一下你想做什么，用户操作的是什么元素？应该建立几个场景？他们的层级关系？如果你像我一样头硬的话就可以开始写了。
* 如果有不明白的，搜索引擎会告诉你，文档会告诉你，实例游戏的源码会告诉你，没有什么解决不了的。

# 下一篇我会说一下我如何进行开发调试，以及游戏的基本结构。


---
title: Hello Cocos (ii)Debugging and Structure
date: 2016-12-03 14:09:06
tags:
- CocosCreator
- Web
- Js
- Game
categories:
- Tech
---
## 接上一篇，我们来谈谈如何进行开发调试，以及我[游戏](http://xuyiwenzhuzhuzhu.cn/game.html)的结构解析。
对于一个project来说，开发与调试的环境是非常重要的，所以我想谈一谈如何在**windows**环境下搭建开发和调试的环境。
同时简单说一说我项目的结构以及设计的思路。

<!--more-->
### 友好开发环境的搭建
千万不要小瞧这一点。一开始我觉得无所谓，用CocosCreator的内置编辑器写代码，没想到遇到了很多不必要的麻烦。
强烈推荐使用VScode及官方插件，不要怕，很好配置。[我是官方教程](http://www.cocos.com/docs/creator/getting-started/coding-setup.html)

如果发布到web端，Chrome浏览器你可少不了。Chrome的console真的非常强大，功能齐全而且界面友好。windows进入chrome按F12进入开发者模式，进console看报错信息，点击报错信息查看详细的代码错误，再和本地服务器上的文件做比对。

### Form the game 如何从零开始思考？
* 你游戏的目的是什么？ **我希望可以做出一个可爱的游戏，同时要尽可能的传达我想对女友传达的**
* 你游戏的主人公是谁？ **两只猪猪是用户主要控制的**
* 想好你怎么接受用户输入了吗？ **键盘和鼠标，因为我是在WebDesktop，所以添加对应的Listener**
* 你大概需要几个场景？ **openScene,helpScene,settingScene,aboutScene,finishScene,gameScene 这个还算好想**
* 你有什么需要重复出现的东西吗？就像怪物？道具？ **猪猪需要吃爱心，还有很多道具，他们需要重复得出现，所以我需要给他们建立prefab**
* 通关条件是什么呢？ **猪猪吃饱就通关啦！**

### 如果你像我一样想好上面的问题 你可以开始动手啦
你大概需要做哪些事情()
* 如果你足够满意，那么恭喜你，return **完成project！**
* 获取贴图资源，精灵纹理，并且用PS修正
* 挑选你中意的BGM，细节决定一切。
* 做好你的场景跳转，利用Button控件。
* 写你的主场景中的用户控制模块。
* 逐步丰满你的游戏内容，加控件，加判定，加新的元素和逻辑。
* return 你大概需要做哪些事情();
没错就是这个递归，我至少递归了五次，每次都有翻天覆地的变化，任何一个以前版本都不忍直视。

### 主场景gameScene的结构解析 会在下一篇文章中附一些代码
![](/images/image/HelloCocos2/1.png)
---
title: DW + Bootstrap 制作响应式静态页面
date: 2016-12-09 13:11:29
tags:
- Bootstrap
- Web
categories:
- Tech
---
## 昨天我用 Dreamweaver+Bootstrap 给自己的静态页面做了一些升级
# 效果拔群
* [我的网站](http://xuyiwenzhuzhuzhu.cn)
* [Dreamweaver官网](https://www.adobe.com/cn/products/dreamweaver.html)
* [Bootstrap是个好东西](http://v3.bootcss.com/getting-started/)

<!--more-->

### 简单的介绍
* Dreamweaver是Adobe全家桶的一员，是一个网页设计的“IDE”，集成了**代码编写**、**网页预览**、**添加组件模块**等等内容。现在和Bootstrap强强联合，用它确实可以提高编写好看的响应式网页的生产力。
* Bootstrap是Twitter的前端程序员们为了方便自己写出好看实用的网页而编写的开源前端框架，内含各种**响应式布局**、**各种样式模板**等等，可以极大地提高网页开发的效率。

### Dreamweaver的使用
Dreamweaver属于adobe全家桶，所以如果弄不清楚怎么下载安装的话请关键词搜索adobe安装。
Dreamweaver有哪些优点？作为之前一直用Atom+Chrome刷新来写静态页面的人，我来总结一下我对DW的上手感受。
* fancy的代码补全和代码高亮，不输Atom。
* 较为方便的项目管理，附加CSS样式表，新建站点等等。
* 可以直接动态地切换视图模式，在**代码**、**拆分**、**实时模式**之间非常方便地切换，真正做到了写代码、预览、调试一体化。
* 很不错的Bootstrap支持。
* 写出来的代码整齐优雅，可读性好。
* 可以任意切换视口(viewport)，写出适应性更强的网页。

### 操作图例
顶部的工具栏、模式切换功能、项目文件的显示，各种颜色的条子是视口的选择，点击用来查看各种设备下的网页响应情况。
![](/images/image/DW/topbar.png)

侧边栏的各种Bootstrap组件(Html的Bootstrap模式下)，以及Html层级关系图。
![](/images/image/DW/sidebar.png)

各种模式的切换，如拆分模式。
![](/images/image/DW/isolate.png)

确实挺能提高生产力的，但你要说你用ATOM+各种插件也可以做到同样的效果，那确实完全没必要用DW。

### 说说Bootstrap
Bootstrap是**移动设备优先的**，在这个移动终端泛滥的年代，Bootstrap不火都不行，它可以让网页在各种终端上达到良好的显示效果。
什么叫良好的显示效果？**你用手机、平板、电脑打开我这个博客你就明白了**。
Bootstrap利用栅格化达到了这一点，它将网页切分成一个一个栅格（rows & cols），恩就像矩阵一样哈哈哈。
```html
<div class="container-fluid">  <!-- 建立一个100%宽度的容器 --> 
  <div class="row"> <!-- 建立一行 -->
    <div class="col-md-6 col-md-offset-3"> <!-- 建立一个占6个单位格的列（一共12个）并且右移3个单位（居中了） -->
      <h1 class="text-center textcolor">It's all about Sally & Jeff</h1>
    </div>
  </div>
</div>
```
这样的“矩阵”会根据你的视口(viewport)产生适当的缩放和响应。
具体的教程请见[Bootstrap栅格化](http://v3.bootcss.com/css/#grid)。

Bootstrap还有各种各样的模块组件，比如[我的网站](http://xuyiwenzhuzhuzhu.cn)的导航栏就是用的Bootstrap的代码，而这些可以很方便地在官方文档中找到，也可以用DW的侧边栏很快速的生成。

### 下面放出网站的整体截图效果 大家可以用手机[我的网页](xuyiwenzhuzhuzhu.cn)打开看看有什么不同 祝大家周末愉快
![](/images/image/DW/zhuzhuzhuupdated.png)
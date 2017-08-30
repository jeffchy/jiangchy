---
title: Hello Cocos (iii)重要操作及一些坑
date: 2016-12-03 15:17:30
tags:
- CocosCreator
- Web
- Js
- Game
categories:
- Tech
---
# 前方代码预警
我会说一些我觉得比较重要的代码
首先，CocosCreator项目地址[Gitbub Source Code](https://github.com/jeffchy/projectzhuzhuzhu-Cocoscreator)
作品项目地址[My Game Your Game]((http://xuyiwenzhuzhuzhu.cn/game.html)
<!--more-->
### 场景跳转时渐入渐出实例
```javascript
        goOpenScene: function(){
        this.node.runAction(cc.sequence(cc.fadeOut(1.0),cc.callFunc(function(){
                    cc.director.loadScene('openScene')
                    })));
        //   cc.director.loadScene('openScene');  
        },
        // use this for initialization
        onLoad: function () {
            this.node.setOpacity(0);
            this.node.runAction(cc.fadeIn(5));
            // fade Effect
        },
```
### 用户输入的listener实例
```javascript
        setInputControl: function(){ // 设定猪猪的左右移动以及跳动的键盘控制
        var self = this;
        cc.eventManager.addListener({
            event: cc.EventListener.KEYBOARD,
            onKeyPressed: function(KeyCode,event){
                switch (KeyCode) {
                    case cc.KEY.a:
                        self.moveRight = false;
                        self.moveLeft = true;
                        break;
                    case cc.KEY.d:
                        self.moveLeft = false;
                        self.moveRight = true;

                        break;
                    case cc.KEY.w:
                        self.jump = true;
                        break;
                    default:
                        // code
                }
            },
            onKeyReleased: function(KeyCode,event){
                switch (KeyCode) {
                    case cc.KEY.a:
                        self.moveLeft = false;
                        break;
                    case cc.KEY.d:
                        self.moveRight = false;
                        break;
                    case cc.KEY.w:
                        self.jump = false;
                        break;
                    default:
                        // code
                }
            }
        },self.node);
        },
```
### 全局变量一直很好用，这样你可以在各个场景访问并且修改变量
建立一个.js文件，如
```javascript
        module.exports = {
        difficulty : 0,
        reveal: 0,
        totalTimer: 0,
        score: 0,
        };
```
在别的文件中访问和修改这些变量
```javascript
        var mydiff = require('difficulty');
        mydiff.difficulty = 100;
```
### 获取一个对象的属性
播放一段序列帧动画
```javascript
        var anim = this.musicNote.getComponent(cc.Animation); // getComponent 获取所有类型为cc.Animation的对象
        anim.play('music'); 
```
### 背景（精灵）材质的替换
```javascript
        onLoad: function () { //
            this.bgPictures = new Array();
            // 建立数组存储所有的图片材质
            
            this.bgPictures[0] = 'Texture/Background/snow.jpg';
            this.bgPictures[1] = 'Texture/Background/paris.jpg';
            this.bgPictures[2] = 'Texture/Background/mona.jpg';
            this.bgPictures[3] = 'Texture/Background/dibai.jpg';
            this.bgPictures[4] = 'Texture/Background/space.jpg';
            // bgPictures[5] = 'Texture/Background/snow.jpg';
            this.bgDark = new Array();
            this.bgDark[0] = 'Texture/dark/flower_dark.jpg';
            this.bgDark[1] = 'Texture/dark/nkg_dark.jpg';
            this.bgDark[2] = 'Texture/dark/shanghai_dark.jpg';
            this.bgDark[3] = 'Texture/dark/sky_dark.jpg';
            this.bgDark[4] = 'Texture/dark/shanghai.jpg';
            this.bgDark[5] = 'Texture/dark/raining.jpg';
            this.bgDark[6] = 'Texture/dark/raining_happy.jpg';
            
        },

        changeBgRandomly: function(){  // 随机切换材质
            this.node.setOpacity(0);    // 渐变效果
            var index = Math.floor(Math.random()*4)  // js的随机函数
            var realUrl = cc.url.raw(this.bgPictures[index]);  // 加入材质
            var texture = cc.textureCache.addImage(realUrl);
            this.getComponent(cc.Sprite).spriteFrame.setTexture(texture);
            this.node.runAction(cc.fadeIn(5));

        },

        changeDarkBg: function(index){
            this.node.setOpacity(0);
            var realUrl = cc.url.raw(this.bgDark[index]);
            var texture = cc.textureCache.addImage(realUrl);
            this.getComponent(cc.Sprite).spriteFrame.setTexture(texture);
            this.node.runAction(cc.fadeIn(5));

        }
```
注意！发布为web的时候这些材质需要手动地拷贝进生成网页里面的res/raw-assets的对应位置，不知道新版本有没有修复这个发布问题

### prefeb的实例化
```javascript
        spawnNewRose: function(){
            // var index = Math.floor(Math.random()*4); // 0 1 2 3
            var newRose = cc.instantiate(this.rosePrefeb); // 实例化
            this.node.addChild(newRose);
            newRose.setPosition(this.getNewStarPosition());
            newRose.getComponent('rose').game = this;

            this.itemTimer = 0;
        },
```
### schedule计时器的使用
```javascript
        jeffGainDoctor:function(){
            // this.score += 10;
            cc.audioEngine.playEffect(this.punishAudio, false);  // 播放音效
            var anim = this.down.getComponent(cc.Animation);    // 播放动画
            anim.play('down');  
            this.player_jeff.getComponent('jeff').speedScale = 0.1;
            this.scheduleOnce(function(){
                this.player_jeff.getComponent('jeff').speedScale = 1;
            },8);  // 利用计时器实现道具效果持续
        },
```

### 代码部分到此结束 会有一篇小总结

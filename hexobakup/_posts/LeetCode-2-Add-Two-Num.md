---
title: LeetCode 2 Add Two Num
date: 2017-02-04 18:12:34
tags:
- LeetCode
- cpp
- Algorithm
categories:
- Code
---
[LeetCode #2 Add Two Num](https://leetcode.com/problems/add-two-numbers/?tab=Description)
<!-- more -->
我又来填坑了，我又被小水题骗了。
唉，我更水啊。
水题都做地蛋疼，同志仍需努力啊。
初看这道题就是把我们的加法变化了一下，两个linklist都是经过reverse的，中间夹杂一些进位呀之类的东西。
当时我的想法也很straight forward，我把两个list都遍历一遍，将其变为数值的形式。然后就可以顺其自然的进行加法运算，最后只要再重新建一个linklist就行了。
理论上没有什么问题，但当我写来写去，string int转来转去之后，提交以后发现1500+个testcase只能过800个，原因太简单了，int爆了呗，long long int也爆了。
一拍脑袋哎呀我好蠢，早就该想到的。这也是他用linklist存储的原因嘛，至于我为什么会想用数字来存，可能就是偷懒了懒得想新的算法，实际上和平时的加法平没有变化，注意，是**几乎完全没有变化！**，不就是镜面对称了一下吗，要进一的进一就行啦。
我就这么被骗了，小学数学没学好，想通这些了以后就很简单了，直接参考了discussion里面vote第一大神的java代码，改成了cpp并且写了一些注释。
好在自己linklist还是满熟练的...就是人傻。

```C++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* c1 = l1; // gethead
        ListNode* c2 = l2;
        ListNode* sentinel = new ListNode(0);  
        ListNode* d = sentinel; //copy 一下头指针的位置，不然之后找不到了
        int sum = 0;
        while (c1 != nullptr || c2 != nullptr) { // 遍历两个链表
            sum /= 10;  // 进一
            if (c1 != nullptr) {
                sum += c1->val;
                c1 = c1->next;
            }
            if (c2 != nullptr) {
                sum += c2->val;
                c2 = c2->next;
            }
            d->next = new ListNode(sum % 10);
            d = d->next;
        }
        if (sum / 10 == 1)
            d->next = new ListNode(1); //最后该进一的进一
        return sentinel->next;
        // 看吧，完全是一模一样的啊 至于他为什么reverse过来，正是为了方便我们啊...题还是要多刷
    }
};
```
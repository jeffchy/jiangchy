---
title: LeetCode 75 Sort Colors
date: 2016-12-17 21:34:45
tags:
- LeetCode
- cpp
- Algorithm
categories:
- Code
---
[LeetCode #75 Sort Colors 脑经急转弯:)](https://leetcode.com/problems/sort-colors/)
<!--more-->
### 题目
```
75. Sort Colors   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 132376 Total Submissions: 362332 Difficulty: Medium Contributors: Admin

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
```
想刷一刷排序题，特意挑了一道中等难度的，没想到直接遇上了脑经急转弯，哈哈哈哈哈哈哈哈哈哈哈哈啊哈哈哈哈
我们来看一看**出题人的阴险之处**。
* Medium难度 让大家以为这题没有多么容易
* Sort分类 满脑子的Qsort,heapSort飞了出来
* 不高的通过率 Excuse me？
* 一本正经地说不给用 std:sort()

是我不专业了，数据结构才学的，这其实就是Counting Sort，不要瞧不起人家，人家O(N)呢，虽然对元素形式有限制。
哈哈哈哈哈哈哈哈哈哈哈哈，太阴了，如果刷题太死，不独立思考，说不定真的会落入出题人的圈♂套。
像我这么机智的人当然不会，3分钟A了，仰天大笑。
### 这题只要数一遍，再输出来就行了

不废话了，上代码。
```C++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int countarr[3] = {0,0,0}; // red white blue
        
        for (int i = 0;i<nums.size();i++){
            countarr[nums[i]]++;
        }
        int red = countarr[0];int white = countarr[1];int blue = countarr[2];
        int temp1 = red + white;int temp2 = red + white + blue;
        for (int i = 0;i<red;i++){nums[i] = 0;}
        for (int i = red;i<temp1;i++){nums[i] = 1;}
        for (int i = temp1;i<temp2;i++){nums[i] = 2;}
    }
};
```
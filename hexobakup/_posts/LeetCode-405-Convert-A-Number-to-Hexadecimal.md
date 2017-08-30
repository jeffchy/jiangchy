---
title: 'LeetCode #405 Convert A Number to Hexadecimal'
date: 2016-12-15 13:16:11
tags:
- LeetCode
- cpp
- Algorithm
categories:
- Code
---
[LeetCode #405 Convert A Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)
<!--more-->
这题我特么WA了两次，气死爸爸了。
### tips：
* 了解**原码**、**反码(one's complement)**、**补码(two's complement)**。
* 了解**位运算(bitwise operation)**。
* 不要被题目的大于零、小于零什么的迷惑！负数基本适配于正数的算法，因为他们本质都是进制进过位运算得到的，这就是补码的优越性，有时间可以自行认真推导一下。

## Bitwise / AC
```C++
class Solution {
public:
    string toHex(int num) {
        string hex_ele[16] = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"};
        string result;
        if (num == 0){result = "0";}
        else if(num > 0){
            while(num != 0){
                result += hex_ele[num & 15];
                num >>= 4;
            }
        }
        else{
            for (int i = 0;i < 8;i++){
                result += hex_ele[num & 15];
                num >>= 4;
            }
        }
        reverse(result.begin(),result.end());
        return result;
    }
};
```
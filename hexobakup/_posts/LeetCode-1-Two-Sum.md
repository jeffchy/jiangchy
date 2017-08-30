---
title: 'LeetCode #1 Two Sum'
date: 2016-12-15 13:10:14
tags:
- LeetCode
- cpp
- Algorithm
categories:
- Code
---
[LeetCode #1 Two Sum](https://leetcode.com/problems/two-sum/)
<!--more-->
# 这题的目的是让一个C-style的Cpper学习STL
## Bruce force / AC
什么？这也能AC？可能给大家一点自信吧。
```C++
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // in a violent way
        vector<int>vec;
        for (int i = 0;i<nums.size();i++){
            int temp = nums[i];
            for (int j = (i+1);j<nums.size();j++){
                if (temp + nums[j] == target){ // check the next else O(n2)
                    vec.push_back(i);
                    vec.push_back(j);
                    break;
                }
            }
        }
        return vec;
    }
};
```

## Hash / AC
unordered_map 是STL中一种哈希容器，提供键值对映射，很好用。详询cplusplus reference。
Hash 可以将查找速度降为O(1)
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // using hash table
        unordered_map<int,int>hashMap;
        vector<int>vec;
        for (int i = 0;i<nums.size();i++){
            hashMap[nums[i]] = i; // simple hash function
            // kay: value val:index
        }
        for (int j = 0;j<nums.size();j++){
            int diff = target - nums[j];
           if (hashMap.find(diff) != hashMap.end() && hashMap[diff] > j) {
                vec.push_back(j);
                vec.push_back(hashMap[diff]);
                break;
            }
        }
        return vec;
    }
};
```
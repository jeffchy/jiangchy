---
title: 'LeetCode #222 Count Complete Binary Tree Element'
date: 2016-12-15 13:14:39
tags:
- LeetCode
- cpp
- Algorithm
categories:
- Code
---
[LeetCode #222 Count Complete Binary Tree Element](https://leetcode.com/problems/count-complete-tree-nodes/)
<!--more-->

## Bruce Force / TLE
Simply use DFS and count, TLE.

```C++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    
    void DFS(TreeNode* root){
        if (root == NULL){return;}
        count ++;
        DFS(root->left);
        DFS(root->right);
    }
    int countNodes(TreeNode* root) {
        DFS(root);
        return count;
        
    }
    
};

```
## Divide and Conquer / AC
分别一直往左、一直往右找高度，若left_depth == right_depth,说明这一棵**subtree**是一棵**complete tree**,可以由公式计算出高度,若不相同，递归 return countNodes(root->left)+countNodes(root->right)+1;相当巧妙。
sigh,对分治的思想和完全树的性质理解地还不够到位。
```C++
class Solution {
public:
    int countLeft(TreeNode *root){
        int left_height = -1;
        while(root!=NULL){
            left_height++;
            root = root->left;
        }
        return left_height;
    }
    
    int countRight(TreeNode *root){
        int right_height = -1;
        while(root!=NULL){
            right_height++;
            root = root->right;
        }
        return right_height;
    }
    
    int countNodes(TreeNode* root) {
        int left_depth = countLeft(root);
        int right_depth = countRight(root);
        
        if (left_depth == right_depth){
            return ((1 << (left_depth+1)) - 1);
        }
        else{
            return countNodes(root->left)+countNodes(root->right)+1;
        }
        
    }
    
};
```
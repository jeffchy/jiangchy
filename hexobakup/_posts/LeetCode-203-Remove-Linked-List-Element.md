---
title: 'LeetCode #203 Remove Linked List Element'
date: 2016-12-15 13:13:56
tags:
- LeetCode
- cpp
- Algorithm
categories:
- Code
---
[LeetCode #203 Remove Linked List Element](https://leetcode.com/problems/remove-linked-list-elements/)
<!--more-->
链表的基础操作稍微改进，不要小看基础题。
# tips:
* 对于链表的删除，牢记一句话：before_ptr->next = current_ptr->next;
* 正由于**不一定有before_ptr**，所以需要分链表头和链表中两种情况。
* 这题要求删除所有的给定值得节点，而绝大部分书上的代码都是只删除一个的，要注意时刻维护before_ptr,current_ptr两个指针。

```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *ptr_current = head;
        ListNode *ptr_before = head;
        // if (ptr == NULL)(return NULL;)
        while(ptr_current != NULL){
            if (ptr_current->val == val && ptr_current == head){
                ListNode *temp = ptr_current;
                ptr_current = ptr_current->next;
                delete temp;
                head = ptr_current;
                ptr_before = ptr_current;
            }
            else if (ptr_current->val == val && ptr_current != head){
                ListNode *temp = ptr_current;
                ptr_current = ptr_current->next;
                ptr_before->next = ptr_current;
                delete temp;
                
                
            }
            else{
                ptr_before = ptr_current;
                ptr_current = ptr_current->next;
            }
        }
        return head;
        
    }
};
```

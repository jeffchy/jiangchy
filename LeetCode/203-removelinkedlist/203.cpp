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
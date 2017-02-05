class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* c1 = l1; // gethead
        ListNode* c2 = l2;
        ListNode* sentinel = new ListNode(0);
        ListNode* d = sentinel;
        int sum = 0;
        while (c1 != nullptr || c2 != nullptr) {
            sum /= 10;
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
            d->next = new ListNode(1);
        return sentinel->next;

    }
};

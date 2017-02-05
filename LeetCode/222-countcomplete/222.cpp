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
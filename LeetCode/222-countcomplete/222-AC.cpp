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
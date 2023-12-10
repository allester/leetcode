/*
https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1116127122/?envType=daily-question&envId=2023-12-09
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        
        vector<TreeNode*> stack;
        vector<int> result;
        TreeNode* curr = root;

        while(curr != nullptr || !stack.empty()) {
            while (curr != nullptr) {
                stack.push_back(curr);
                curr = curr->left;
            }
            curr = stack.back();
            stack.pop_back();
            result.push_back(curr->val);
            curr = curr->right;
        }
        return result;
    }
};
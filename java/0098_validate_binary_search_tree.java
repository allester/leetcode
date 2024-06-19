/*
https://leetcode.com/problems/validate-binary-search-tree/submissions/1293952205/
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return _isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean _isValidBST(TreeNode node, long min, long max) {
        if (node == null) {
            return true;
        }

        boolean left = node.left == null || (node.left != null && min < node.left.val && node.left.val < node.val) ? true : false;
        boolean right = node.right == null || (node.right != null && max > node.right.val && node.right.val > node.val) ? true : false;

        return left && right && _isValidBST(node.left, min, node.val) && _isValidBST(node.right, node.val, max);
    }
}
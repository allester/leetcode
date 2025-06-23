'''
https://leetcode.com/problems/balanced-binary-tree/submissions/1673174652/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _isBalanced(node):
            if not node:
                return 0
            left = _isBalanced(node.left)
            right = _isBalanced(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return _isBalanced(root) != -1
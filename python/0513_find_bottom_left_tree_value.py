'''
https://leetcode.com/problems/find-bottom-left-tree-value/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Q = [root]
        while Q:
            curr = Q.pop(0)
            if curr.right:
                Q.append(curr.right)
            if curr.left:
                Q.append(curr.left)
        return curr.val
'''
https://leetcode.com/problems/range-sum-of-bst/submissions/1140886665/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        s = [root]
        while s:
            curr = s.pop()
            if low <= curr.val <= high:
                res += curr.val
            if curr.left:
                s.append(curr.left)
            if curr.right:
                s.append(curr.right)
        return res
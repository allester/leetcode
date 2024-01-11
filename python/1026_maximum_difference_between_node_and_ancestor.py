'''
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/submissions/1143591379/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #(node, min, max)
        s = [(root, root.val, root.val)]
        ans = -1
        while s:
            curr, dmin, dmax = s.pop()
            ans = max(ans, abs(dmin - curr.val), abs(dmax - curr.val))
            if curr.left:
                s.append((curr.left, min(dmin, curr.val), max(dmax, curr.val)))
            if curr.right:
                s.append((curr.right, min(dmin, curr.val), max(dmax, curr.val)))
        return ans
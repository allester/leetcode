'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1141800424/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st = [(root, 1)]
        ans = 0
        while st:
            curr, depth = st.pop()
            ans = max(ans, depth)
            if curr.left:
                st.append((curr.left, depth+1))
            if curr.right:
                st.append((curr.right, depth+1))
        return ans
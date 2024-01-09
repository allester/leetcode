'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/1141804910/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        st = [(root, root.val)]
        ans = 0
        while st:
            curr, maxval = st.pop()
            if curr.val >= maxval:
                ans += 1
            if curr.left:
                st.append((curr.left, max(maxval, curr.val)))
            if curr.right:
                st.append((curr.right, max(maxval, curr.val)))
        return ans
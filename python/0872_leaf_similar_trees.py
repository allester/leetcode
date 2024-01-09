'''
https://leetcode.com/problems/leaf-similar-trees/submissions/1141762967/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        sq1 = []
        st = [root1]
        while st:
            curr = st.pop()
            if curr.left:
                st.append(curr.left)
            if curr.right: 
                st.append(curr.right)
            if not (curr.left or curr.right):
                sq1.append(curr.val)
        
        sq2 = []
        st = [root2]
        while st:
            curr = st.pop()
            if curr.left:
                st.append(curr.left)
            if curr.right: 
                st.append(curr.right)
            if not (curr.left or curr.right):
                sq2.append(curr.val)

        return sq1 == sq2
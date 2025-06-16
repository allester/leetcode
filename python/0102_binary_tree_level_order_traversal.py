'''
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1666548232/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = [[root.val]]
        q = collections.deque([root])
        while q:
            level = []
            while q:
                curr = q.popleft()
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
            if level:
                levels.append([node.val for node in level])
                q.extend(level)
        return levels
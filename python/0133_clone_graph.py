'''
https://leetcode.com/problems/clone-graph/submissions/1668759999/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(oldNode):
            if oldNode in oldToNew:
                return oldToNew[oldNode]
            newNode = Node(oldNode.val)
            oldToNew[oldNode] = newNode
            for oldNeighbor in oldNode.neighbors:
                newNode.neighbors.append(dfs(oldNeighbor))
            return newNode
        return dfs(node) if node else None
        
        
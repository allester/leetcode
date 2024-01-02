'''
https://leetcode.com/problems/assign-cookies/submissions/1134787524/
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for cookie in s:
            if cookie >= g[i]:
                i += 1
            if i == len(g):
                return i
        return i
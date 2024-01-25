'''
https://leetcode.com/problems/isomorphic-strings/submissions/1156169019/
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        for (si, ti) in zip(s, t):
            if si not in d:
                d[si] = ti
            
            if d[si] != ti:
                return False
        return len(d) == len(set(d.values()))
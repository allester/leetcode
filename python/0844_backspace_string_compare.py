'''
https://leetcode.com/problems/backspace-string-compare/submissions/1201671344/
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S = []
        for c in s:
            if c != '#':
                S.append(c)
            elif S:
                S.pop()

        T = []
        for c in t:
            if c != '#':
                T.append(c)
            elif T:
                T.pop()
        
        return S == T
'''
https://leetcode.com/problems/find-the-difference/submissions/1156110466/
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26
        for c in s:
            i = ord(c) - 97
            count[i] += 1
        for c in t:
            i = ord(c) - 97
            count[i] -= 1
            if count[i] < 0:
                return c
        return ''
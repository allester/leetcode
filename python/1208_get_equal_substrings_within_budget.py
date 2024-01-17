'''
https://leetcode.com/problems/get-equal-substrings-within-budget/submissions/1148982550/
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = 0
        l, r = -1, 0
        maxLength = 0
        while r < len(s):
            cost += abs(ord(s[r]) - ord(t[r]))
            while cost > maxCost:
                l += 1
                cost -= abs(ord(s[l]) - ord(t[l]))
            maxLength = max(maxLength, r - l)
            r += 1
        return maxLength
'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1663144470/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v = set()
        i = -1
        max_j = 0
        for j in range(len(s)):
            while s[j] in v:
                i += 1
                v.remove(s[i])
            v.add(s[j])
            max_j = max(max_j, j-i)
        return max_j
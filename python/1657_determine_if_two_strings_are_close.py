'''
https://leetcode.com/problems/determine-if-two-strings-are-close/submissions/1137796116/
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = dict()
        d2 = dict()
        for c in word1: d1[c] = d1.get(c, 0) + 1
        for c in word2: d2[c] = d2.get(c, 0) + 1
        return sorted(d1.values()) == sorted(d2.values()) and set(d1.keys()) == set(d2.keys())
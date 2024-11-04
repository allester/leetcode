'''
https://leetcode.com/problems/string-compression-iii/submissions/1443069051/
'''

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        prev = word[0]
        i = 0
        for c in word:
            if c == prev and i < 9:
                i += 1
            else:
                comp += str(i) + prev
                i = 1
            prev = c
        comp += str(i) + prev
        return comp
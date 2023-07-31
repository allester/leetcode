'''
https://leetcode.com/problems/ransom-note/submissions/1002977889/
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        for letter in magazine:
            d[letter] = d.get(letter,0) + 1

        for letter in ransomNote:
            if d.get(letter, 0):
                d[letter] -= 1
            else:
                return False
        return True
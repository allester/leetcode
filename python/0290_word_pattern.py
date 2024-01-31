'''
https://leetcode.com/problems/word-pattern/submissions/1161648742/
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        d = dict()
        s = s.split()
        words = set()
        if len(pattern) != len(s):
            return False
        for (char, word) in zip(pattern, s):
            if char not in d:
                if word in words:
                    return False
                d[char] = word
                words.add(word)
            elif d[char] != word:
                return False
        return True
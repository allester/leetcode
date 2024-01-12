'''
https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/1144347533/
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels =  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count1 = count2 = 0
        n = len(s)
        for i in range(0, n//2):
            if s[i] in vowels:
                count1 += 1
        for i in range(n//2, n):
            if s[i] in vowels:
                count2 += 1
        return count1 == count2
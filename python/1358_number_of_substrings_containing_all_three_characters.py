'''
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/submissions/1726287868/?envType=daily-question&envId=2025-08-07
'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        left = 0
        char = {'a': 0, 'b': 0, 'c': 0}
        for right in range(n):
            char[s[right]] += 1
            while (char['a'] > 0 and char['b'] > 0 and char['c'] > 0):
                count += n - right
                char[s[left]] -= 1
                left += 1
        return count
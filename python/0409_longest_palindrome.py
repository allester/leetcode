'''
https://leetcode.com/problems/longest-palindrome/submissions/1003958881/
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        T = set()
        count = 0
        for char in s:
            if char not in T:
                T.add(char)
            else:
                T.remove(char)
                count += 2
        if T:
            count += 1
        return count
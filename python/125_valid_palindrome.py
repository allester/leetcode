'''
https://leetcode.com/problems/valid-palindrome/submissions/983293301/
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for char in s:
            if char.isalnum():
                clean += char
        clean = clean.lower()
        return clean == clean[::-1]
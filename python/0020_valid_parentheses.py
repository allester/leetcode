'''
https://leetcode.com/problems/valid-parentheses/submissions/983265066/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for char in s:
            if char in d:
                stack.append(char)
                continue

            if not stack:
                return False

            else:
                last = stack.pop()
                if char != d[last]:
                    return False
        return len(stack) == 0
'''
https://leetcode.com/problems/string-to-integer-atoi/submissions/1675544995/
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        N = len(s)
        i = 0
        while i < N and s[i] == ' ':
            i += 1
        stack = []
        neg = False
        if i < N and s[i] == '-':
            neg = True
            i += 1
        elif i < N and s[i] == '+':
            i += 1
        
        while i < N and s[i].isnumeric():
            stack.append(s[i])
            i += 1
        if stack:
            res = (-1 if neg else 1) * int(''.join(stack))
            if res < - 2**31:
                return -2**31
            if res > 2**31-1:
                return 2**31-1
            return res
        return 0
'''
https://leetcode.com/problems/add-strings/submissions/1156117223/
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        n = len(num1)
        m = len(num2)
        i = 0
        carry = 0
        ans = ''
        while i < n or i < m:
            a = b = 0
            if i < n:
                a = int(num1[i])
            if i < m:
                b = int(num2[i])
            ab = a + b + carry
            if carry > 0:
                carry -= 1
            if ab > 9:
                carry = 1
                ab -= 10
            ans = str(ab) + ans
            i += 1
        if carry:
            ans = str(carry) + ans
        return ans
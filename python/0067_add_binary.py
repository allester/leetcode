'''
https://leetcode.com/problems/add-binary/submissions/1016020260/
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ''
        while i >= 0 or j >= 0:
            digit = carry
            if i >= 0: 
                digit += int(a[i])
                i -= 1
            if j >= 0:
                digit += int(b[j])
                j -= 1
            carry = 1 if digit > 1 else 0
            result = str(digit % 2) + result

        if carry: 
            result = str(carry) + result

        return result
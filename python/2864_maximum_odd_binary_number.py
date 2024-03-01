'''
https://leetcode.com/problems/maximum-odd-binary-number/
'''

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        zeros = 0
        for num in s:
            if num == '1':
                ones += 1
            else:
                zeros += 1

        return '1' * (ones - 1) + '0' * zeros + '1'
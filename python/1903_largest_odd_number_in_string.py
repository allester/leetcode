'''
https://leetcode.com/problems/largest-odd-number-in-string/submissions/1245981975/
'''


class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while (i > -1):
            if (int(num[i]) % 2 == 1):
                break
            i -= 1
        return num[0:i+1]
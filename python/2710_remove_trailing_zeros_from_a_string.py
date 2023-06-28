'''
https://leetcode.com/submissions/detail/978863522/
'''

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.strip('0')
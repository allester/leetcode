'''
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/submissions/1713958951/?envType=daily-question&envId=2025-07-28
'''
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(16, -1, -1):
            p = 3 ** i
            if n >= p:
                n -= p
        return n == 0
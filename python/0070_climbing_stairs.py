'''
https://leetcode.com/problems/climbing-stairs/submissions/1150882545/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        T = [0, 1, 2, 3] + [0] * (n-3)
        for i in range(4, len(T)):
            T[i] = T[i-1] + T[i-2]
        return T[n]

        
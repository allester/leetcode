'''
https://leetcode.com/problems/unique-paths/submissions/1676601654/
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        T = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            T[i][0] = 1
        for j in range(n):
            T[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = T[i-1][j] + T[i][j-1]

        return T[-1][-1]
        
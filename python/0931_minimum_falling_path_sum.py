'''
https://leetcode.com/problems/minimum-falling-path-sum/
'''

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        T = [[0 for i in range(n)] for j in range(n)]
        T[0] = matrix[0]
        for i in range(1, n):
            for j in range(n):
                T[i][j] = T[i-1][j] + matrix[i][j]
                if j > 0:
                    T[i][j] = min(T[i][j], T[i-1][j-1] + matrix[i][j])
                if j < n-1:
                    T[i][j] = min(T[i][j], T[i-1][j+1] + matrix[i][j])
        return min(T[-1])
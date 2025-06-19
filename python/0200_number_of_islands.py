'''
https://leetcode.com/problems/number-of-islands/submissions/1668827845/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        count = 0
        def dfs(i, j):
            s = [(i, j)]
            while s:
                i, j = s.pop()
                grid[i][j] = '0'
                for (_i, _j) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    if 0 <= i+_i < N and 0 <= j+_j < M and grid[i+_i][j+_j] == '1':
                        s.append((i+_i, j+_j))
                
        for (i, j) in ((i, j) for i in range(N) for j in range(M) if grid[i][j] == '1'):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

        return count
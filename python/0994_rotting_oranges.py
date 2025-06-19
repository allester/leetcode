'''
https://leetcode.com/problems/rotting-oranges/submissions/1668837438/
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        minutes = 0
        fresh = 0
        q = deque()
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for _i, _j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= i+_i < N and 0 <= j+_j < M and grid[i+_i][j+_j] == 1:
                        grid[i+_i][j+_j] = 2
                        q.append((i+_i, j+_j))
                        fresh -= 1

        return minutes if fresh == 0 else -1
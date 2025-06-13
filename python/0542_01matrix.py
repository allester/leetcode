'''
https://leetcode.com/problems/01-matrix/submissions/1662511855/
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = collections.deque((i, j) for i in range(m) for j in range(n) if mat[i][j] == 0)
        
        ans = [[-1 if mat[i][j] == 1 else 0 for j in range(n)] for i in range(m)]

        while q:
            i, j = q.popleft()
            for _i, _j in ((i, j+1), (i, j-1), (i-1, j), (i+1, j)):
                if 0 <= _i < m and 0 <= _j < n and ans[_i][_j] == -1:
                    ans[_i][_j] = ans[i][j] + 1
                    q.append((_i, _j))

        return ans

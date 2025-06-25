'''
https://leetcode.com/problems/spiral-matrix/submissions/1675567290/
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        def _spiral(i_begin, i_end, j_begin, j_end, direction):
            if i_begin > i_end or j_begin > j_end:
                return
            match direction:
                case 'up':
                    ans.extend([matrix[i][j_begin] for i in range(i_end, i_begin-1, -1)])
                    j_begin += 1
                    direction = 'right'
                case 'down':
                    ans.extend([matrix[i][j_end] for i in range(i_begin, i_end+1)])
                    j_end -= 1
                    direction = 'left'
                case 'left':
                    ans.extend(matrix[i_end][j_begin:j_end+1][::-1])
                    i_end -= 1
                    direction = 'up'
                case 'right':
                    ans.extend(matrix[i_begin][j_begin:j_end+1])
                    i_begin += 1
                    direction = 'down'
            _spiral(i_begin, i_end, j_begin, j_end, direction)
        _spiral(0, len(matrix)-1, 0, len(matrix[0])-1, 'right')
        return ans
        
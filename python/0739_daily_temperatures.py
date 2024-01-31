'''
https://leetcode.com/problems/daily-temperatures/submissions/1162196616/
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        s = (t, i)
        0 [(73, 0)]
        1 peek t[0] since 74 > 73 - t[1] => 1 push (74, 1)
        2 peek 75 > 74 s[1] = 1 push (75, 2)
        3 peek 75 !> 71 push ((71, 3))
        4 peek 71 !> 69 push (69, 4)
        5 pekk 72 > 69 s[4] = i - t[1] 72 > 71 s[3] = 2
        '''
        N = len(temperatures)
        T = [0] * N
        s = [(temperatures[0], 0)]
        for i in range(1, N):
            t_i = temperatures[i]
            if not s:
                s.append((t_i, i))
                continue
            while s:
                t_j, j = s[-1]
                if t_i > t_j:
                    s.pop()
                    T[j] = i - j
                else:
                    break
            s.append((t_i, i))
        return T
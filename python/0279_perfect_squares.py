'''
https://leetcode.com/problems/perfect-squares/submissions/1169940449/
'''

class Solution:
    def numSquares(self, n: int) -> int:
        '''
        T = []
        j = 1
        0 1 2 3 4 5 6 7 8 9 10 11 12
        0 - - - - - - - - - -  -  -
        0 1 - - - - - - - - -  -  -
        0 1 2
        0 1 2 3
        0 1 2 3 1 2
        j = 2

        T[i] = min(T[i], 1 + T[i - (j * j)])
        '''
        T = [float('inf')] * (n+1)
        T[0] = 0
        
        for i in range(1, n+1):
            j = 1
            while i >= j * j:
                T[i] = min(T[i], T[i - j * j] + 1)
                j += 1
        
        return T[-1]
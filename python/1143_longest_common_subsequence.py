'''
https://leetcode.com/problems/longest-common-subsequence/submissions/1156629545/
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) + 1
        m = len(text2) + 1
        T = [[0 for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if text1[i - 1] == text2[j - 1]:
                    T[i][j] = T[i -1][j-1] + 1
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])
        print(T)
        return T[-1][-1]
'''
https://leetcode.com/problems/count-total-number-of-colored-cells/submissions/1713962082/?envType=daily-question&envId=2025-07-28
'''
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n-1) + 1
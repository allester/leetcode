'''
https://leetcode.com/problems/equal-row-and-column-pairs/submissions/1140938799/
'''

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        ans = 0
        for row in grid: d[tuple(row)] += 1
        for col in zip(*grid): ans += d[tuple(col)]
        return ans
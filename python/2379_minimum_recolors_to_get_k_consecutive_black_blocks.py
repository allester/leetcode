'''
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/submissions/1713982141/?envType=daily-question&envId=2025-07-28
'''
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        for i in range(k):
            if blocks[i] == 'W':
                w += 1
        minW = w
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                w += 1
            if blocks[i-k] == 'W':
                w -= 1
            minW = min(minW, w)
        return minW
'''
https://leetcode.com/problems/maximum-length-of-pair-chain/
'''

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        prev_r = -1001
        ans = 0
        for (l, r) in pairs:
            if l > prev_r:
                ans += 1
                prev_r = r
        return ans
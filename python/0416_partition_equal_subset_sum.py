'''
https://leetcode.com/problems/partition-equal-subset-sum/submissions/1675534452/
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        TOTAL = sum(nums)
        if TOTAL % 2 != 0:
            return False
        T = [False] * (TOTAL // 2 + 1)
        T[0] = True
        N = len(T)
        for num in nums:
            for i in range(N-1, num-1, -1):
                if T[i] or i - num < 0:
                    continue
                T[i] = T[i-num]
        return T[-1]
        
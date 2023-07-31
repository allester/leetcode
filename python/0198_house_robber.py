'''
https://leetcode.com/submissions/detail/980653563/
'''

class Solution:
    def rob(self, nums):
        N = len(nums)
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums)
        T = [0] * N
        T[0], T[1] = nums[0], nums[1]
        for i in range(2, N):
            T[i] = max(T[i-1], T[i-2] + nums[i], T[i-3] + nums[i])
        return max(T)
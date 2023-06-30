class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        T = [0] * N
        T[0] = nums[0]
        for i in range(1,N):
            T[i] = max(T[i-1] + nums[i], nums[i])
        print(T)
        return max(T)
'''
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/submissions/1713949048/?envType=daily-question&envId=2025-07-28
'''
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def bitwise_or(nums):
            bitwise = 0
            for num in nums:
                bitwise |= num
            return bitwise

        max_bitwise = bitwise_or(nums)
        ans = 0

        for r in range(1, len(nums)+1):
            for subset in itertools.combinations(nums, r):
                if bitwise_or(subset) == max_bitwise:
                    ans += 1
        return ans
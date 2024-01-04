'''
https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/1136977815/
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            x = nums[l] + nums[r]
            if x == k:
                l += 1
                r -= 1
                ans += 1
            elif x < k:
                l += 1
            else:
                r -= 1
        return ans
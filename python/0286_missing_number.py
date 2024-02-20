'''
https://leetcode.com/problems/missing-number/submissions/1181287123/?envType=daily-question&envId=2024-02-20
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
'''
https://leetcode.com/problems/majority-element/submissions/1016024226/
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1
        m = len(nums) / 2
        for key, value in d.items():
            if value > m:
                return key
        return -1
'''
https://leetcode.com/problems/majority-element/submissions/1005021692/
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
'''
https://leetcode.com/problems/rearrange-array-elements-by-sign/submissions/1175335181/
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        
        nums[::2] = pos
        nums[1::2] = neg
        
        return nums
'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1006534375/
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashtable = set()
        j = 0
        for i in range(len(nums)):
            if nums[i] not in hashtable:
                hashtable.add(nums[i])
                nums[j] = nums[i]
                j += 1
        return j
        
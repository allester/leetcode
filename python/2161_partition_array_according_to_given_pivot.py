'''
https://leetcode.com/problems/partition-array-according-to-given-pivot/submissions/1713956996/?envType=daily-question&envId=2025-07-28
'''
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        pivots = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                pivots.append(num)
        return less + pivots + greater
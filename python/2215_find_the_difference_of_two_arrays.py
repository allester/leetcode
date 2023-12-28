"""
https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1130689491/
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n = set(nums1)
        m = set(nums2)
        return [list(n-m), list(m-n)]
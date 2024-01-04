'''
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/submissions/1136957504/
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1

        ans = 0
        for value in d.values():
            if value == 1:
                return -1
            ans += math.ceil(value / 3)
        return ans
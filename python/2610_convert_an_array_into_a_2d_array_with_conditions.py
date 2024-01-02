'''
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/submissions/1134259977/
'''

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = dict()
        n = 0
        for num in nums:
            m = d.get(num, 0) + 1
            d[num] = m
            n = max(n, m)
        ans = [[] for _ in range(n)]
        for (key, value) in d.items():
            for i in range(value):
                ans[i].append(key)
        return ans
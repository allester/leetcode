'''
https://leetcode.com/problems/subsets/submissions/1675576829/
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visted = set()
        def _dfs(nums):
            if nums in visted:
                return
            ans.append(nums)
            visted.add(nums)
            for i in range(len(nums)):
                _dfs(nums[:i] + nums[i+1:])
        _dfs(tuple(nums))
        return ans
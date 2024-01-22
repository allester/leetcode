'''
https://leetcode.com/problems/set-mismatch/submissions/1153822674/
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        occ = set()
        ans = [0, 0]
        for num in nums:
            if num in occ:
                ans[0] = num
            else:
                occ.add(num)
        ans[1] = int((n*(n+1)/2) - sum(occ))
        return ans
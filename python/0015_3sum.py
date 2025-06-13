'''
https://leetcode.com/problems/3sum/submissions/1663170170/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        nums.sort()
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = N - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return ans
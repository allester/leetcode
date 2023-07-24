'''
https://leetcode.com/problems/majority-element/submissions/1003009333/
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        m = len(nums) / 2
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > m:
                return num
        return None

'''
Trivial: https://leetcode.com/problems/majority-element/submissions/1003010084/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
'''


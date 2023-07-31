'''
https://leetcode.com/submissions/detail/980290546/
'''

class Solution:
    def containsDuplicate(self, nums):
        hashtable = set()
        for num in nums:
            if num not in hashtable:
                hashtable.add(num)
            else:
                return True
        return False
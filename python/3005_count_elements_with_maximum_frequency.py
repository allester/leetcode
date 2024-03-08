'''
https://leetcode.com/problems/count-elements-with-maximum-frequency/submissions/1197774437/
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        A = [0] * 101

        maxFreq = 0
        for num in nums:
            A[num] += 1
            if A[num] > maxFreq:
                maxFreq = A[num]

        count = 0
        for a in A:
            if a == maxFreq:
                count += a
        
        return count
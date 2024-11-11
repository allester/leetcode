'''
https://leetcode.com/problems/grumpy-bookstore-owner/submissions/1449936114/?envType=daily-question&envId=2024-11-11
'''

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # get default
        N = len(customers)
        satisfied = 0
        for i in range(N):
            if not grumpy[i]:
                satisfied += customers[i]
        max_satisfied = satisfied

        # init sliding window
        for i in range(minutes):
            if grumpy[i]:
                satisfied += customers[i]
        max_satisfied = max(max_satisfied, satisfied)

        # slide the window
        M = N - minutes
        for i in range(M):
            if grumpy[i]:
                satisfied -= customers[i]
            if grumpy[i + minutes]:
                satisfied += customers[i + minutes]
            max_satisfied = max(max_satisfied, satisfied)

        return max_satisfied
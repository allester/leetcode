'''
https://leetcode.com/problems/min-cost-climbing-stairs/submissions/1196893273/
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)

        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])

        return cost[-1]
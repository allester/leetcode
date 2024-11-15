'''
https://leetcode.com/problems/most-profit-assigning-work/submissions/1452852938/?envType=daily-question&envId=2024-11-14
'''

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(list(zip(difficulty, profit)))
        worker.sort()

        max_profit = 0
        best_profit = 0
        i = 0

        for w in worker:
            while i < len(jobs) and w >= jobs[i][0]:
                best_profit = max(best_profit, jobs[i][1])
                i += 1
            max_profit += best_profit

        return max_profit
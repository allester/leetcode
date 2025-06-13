'''
https://leetcode.com/problems/insert-interval/submissions/1662435686/
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        N = len(intervals)
        i = 0

        # add non merges
        while i < N and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        # merge then add
        while i < N and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        ans.append(newInterval)

        # add remaining non merges
        while i < N:
            ans.append(intervals[i])
            i += 1

        return ans
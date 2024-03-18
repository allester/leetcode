'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])

        e1 = points[0][1]
        ans = 1
        
        for s2, e2 in points[1:]:
            if s2 > e1:
                e1 = e2
                ans += 1
        
        return ans
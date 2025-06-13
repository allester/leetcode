'''
https://leetcode.com/problems/k-closest-points-to-origin/submissions/1663131554/
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point:point[0]**2+point[1]**2)
        return points[:k]
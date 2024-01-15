'''
https://leetcode.com/problems/find-players-with-zero-or-one-losses/submissions/1147095069/
'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = dict()
        for w, l in matches:
            d[w] = d.get(w, 0)
            d[l] = d.get(l, 0) + 1
        
        ans = [[], []]
        for key, value in sorted(d.items()):
            if value == 0:
                ans[0].append(key)
            if value == 1:
                ans[1].append(key)
        
        return ans
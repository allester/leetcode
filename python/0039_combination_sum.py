'''
https://leetcode.com/problems/combination-sum/submissions/1668864945/
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0
        ans = []

        def search(combination, i, total):
            if total == target:
                ans.append(combination.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            combination.append(candidates[i])
            search(combination, i, total + candidates[i])
            combination.pop()
            search(combination, i+1, total)

        search([], 0, 0)
        
        return ans
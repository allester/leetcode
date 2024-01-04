'''
https://leetcode.com/problems/unique-number-of-occurrences/submissions/1136982658/
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()
        for num in arr:
            d[num] = d.get(num, 0) + 1
        values = d.values()
        return len(values) == len(set(values))
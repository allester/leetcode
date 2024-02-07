'''
https://leetcode.com/problems/sort-characters-by-frequency/submissions/1169135051/
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        count of each letter
        ''
        d = {'letter' : count}
        list(d.items())
        [['letter', count], ..., [..., ...]]
        sort this
        iterate through
        '''
        D = dict()
        for l in s:
            D[l] = D.get(l, 0) + 1

        letters = list(D.items())
        letters.sort(key = lambda x: x[1], reverse=True)
        
        ans = ''
        for letter, count in letters:
            ans = ans + (letter * count)
        
        return ans
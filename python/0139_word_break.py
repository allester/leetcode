'''
https://leetcode.com/problems/word-break/submissions/1675508046/
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        steps = set(len(word) for word in wordDict)
        wordDict = set(wordDict)
        N = len(s)
        T = [False] * (N + 1)
        T[0] = True
        for i in range(min(steps), N+1):
            for j in steps:
                if i - j < 0:
                    continue
                T[i] = T[i-j] and s[i-j:i] in wordDict
                if T[i]:
                    break
        return T[-1]
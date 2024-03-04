'''
https://leetcode.com/problems/bag-of-tokens/submissions/1193795955/
'''

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = score = 0
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        while i <= j:
            if tokens[i] <= power:
                #play face up
                power -= tokens[i]
                score += 1
                i += 1
            elif score > 0:
                #play face down
                power += tokens[j]
                score -= 1
                j -= 1

            else:
                break
                
            if max_score < score:
                max_score = score

        return max_score
            
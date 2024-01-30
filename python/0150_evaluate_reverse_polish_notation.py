'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1160671846/
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == '+':
                s[-1] = s[-2] + s.pop()
            elif token == '-':
                s[-1] = s[-2] - s.pop()
            elif token == '*':
                s[-1] = s[-2] * s.pop()
            elif token == '/':
                s[-1] = int(s[-2] / s.pop())
            else:
                s.append(int(token))
        return s[0]
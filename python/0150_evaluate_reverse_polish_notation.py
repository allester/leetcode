'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1668765208/
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token.isnumeric() or len(token) > 1:
                nums.append(int(token))
            else:
                y = nums.pop()
                x = nums.pop()
                match (token):
                    case '+':
                        num = x + y
                    case '-':
                        num = x - y
                    case '*':
                        num = x * y
                    case '/':
                        num = int(x / y)
                nums.append(num)
        return nums[0]
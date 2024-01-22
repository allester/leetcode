'''
https://leetcode.com/problems/implement-stack-using-queues/submissions/1153859219/
'''

class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x: int) -> None:
        q2 = []
        while self.q1:
            q2.append(self.q1.pop(0))
        self.q1.append(x)
        while q2:
            self.q1.append(q2.pop(0))

    def pop(self) -> int:
        val = self.q1.pop(0)
        q2 = []
        while q2:
            self.q1.append(q2.pop(0))
        return val

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
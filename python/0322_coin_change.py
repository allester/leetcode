'''
https://leetcode.com/problems/coin-change/submissions/1668798764/
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        T = [amount + 1] * (amount + 1)
        T[0] = 0
        for i in range(1,  amount + 1):
            for coin in coins:
                j = i - coin
                if j >= 0:
                    T[i] = min(T[j] + 1, T[i])
        return T[amount] if T[amount] < amount + 1 else -1
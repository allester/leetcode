'''
https://leetcode.com/submissions/detail/980283400/
'''

class Solution:
    def maxProfit(self, prices):
        min_buy = float('infinity')
        max_profit = 0
        for price in prices:
            if min_buy > price:
                min_buy = price
            elif price - min_buy > max_profit:
                max_profit = price - min_buy
        return max_profit
//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1037066071/

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_buy: i32 = prices[0];
        let mut max_profit: i32 = 0;
        for price in prices {
            if min_buy > price {
                min_buy = price;
            }
            if price - min_buy > max_profit {
                max_profit = price - min_buy;
            }
        }
        max_profit
    }
}
/*
https://leetcode.com/problems/buy-two-chocolates/submissions/1124489612/
*/

class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int c1 = INT_MAX, c2 = INT_MAX;
        for (const int& price : prices) {
            if (price < c2) c2 = price;
            if (c2 < c1) swap(c1, c2);
        }
        int result = money - c1 - c2;
        if (result >= 0) return result;
        return money;
    }
};
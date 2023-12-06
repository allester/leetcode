/*
https://leetcode.com/problems/calculate-money-in-leetcode-bank/submissions/1113798414/
*/

class Solution {
public:
    int totalMoney(int n) {
        int r = n % 7;
        int k = n / 7;
        int total = 0;
        for (int i = 0; i < r; i++) {
            total += i + 1;
        }
        total += k * 28 + r * k;
        for (int i = 0; i < k; i++){
            total += i * 7;
        }
        return total;
    }
};
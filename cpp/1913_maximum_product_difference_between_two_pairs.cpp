/*
https://leetcode.com/problems/maximum-product-difference-between-two-pairs/submissions/1122762214/
*/

class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int num1, num2, num3, num4;
        num1 = num2 = INT_MIN;
        num3 = num4 = INT_MAX;
        for (const int& num : nums) {
            if (num >= num1) num1 = num;
            if (num1 >= num2) swap(num1, num2);
            if (num <= num3) num3 = num;
            if (num3 <= num4) swap(num3, num4);
        }
        return (num1 * num2) - (num3 * num4);
    }
};
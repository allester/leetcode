/*
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/1118178638/
*/

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        int max_i = INT_MIN;
        for (int k = 0; k < n; k++) {
            if (nums[k] > max_i) {
                max_i = nums[k];
                i = k;
            }
        }
        int j = 0;
        int max_j = INT_MIN;
        for (int k = 0; k < n; k++) {
            if (nums[k] > max_j && i != k) {
                max_j = nums[k];
                j = k;
            }
        }
        return (max_i - 1) * (max_j - 1);
    }
};
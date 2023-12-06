/*
https://leetcode.com/problems/product-of-array-except-self/submissions/1113860875/
*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> output(n, 1);
        int left = 1;
        for (int i = 0; i < n; i++) {
          output[i] *= left;
          left *= nums[i];
        }
        int right = 1;
        for (int i = n - 1; i > -1; i--) {
          output[i] *= right;
          right *= nums[i];
        }
        return output;
    }
};
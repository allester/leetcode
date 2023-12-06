/*
https://leetcode.com/problems/increasing-triplet-subsequence/submissions/1113869645/
*/

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        int i = INT_MAX;
        int j = INT_MAX;
        for (int idx = 0; idx < n; idx++) {
            if (nums[idx] <= i) {
                i = nums[idx];
            } else if (nums[idx] <= j) {
                j = nums[idx];
            } else {
                return true;
            }
        }
        return false;
    }
};
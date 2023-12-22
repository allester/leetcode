/*
https://leetcode.com/problems/find-peak-element/submissions/1125469051/
*/

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int i = l + (r - l) / 2;
            if (nums[i] < nums[i+1]) l = i + 1;
            else r = i;  
        }
        return l;
    }
};
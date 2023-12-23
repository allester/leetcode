/*
https://leetcode.com/problems/find-pivot-index/submissions/1126013257/
*/

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        const int n = nums.size();
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        for (int i = 1; i < n; i++) left[i] = left[i-1] + nums[i-1];
        for (int i = n - 2; i >= 0; i--) right[i] = right[i+1] + nums[i+1];
        for (int i = 0; i < n; i++) if (left[i] == right[i]) return i;
        return -1;
    }
};
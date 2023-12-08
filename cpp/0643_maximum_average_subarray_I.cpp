/*
https://leetcode.com/problems/maximum-average-subarray-i/submissions/1115297597/
*/

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double avg_max;
        double avg;
        double numerator = 0;
        int n = nums.size();
        int i = 0;
        while (i < k) {
            numerator += nums[i];
            i++;
        }
        avg_max = numerator / k;
        while (i < n) {
            numerator -= nums[i-k];
            numerator += nums[i];
            avg = numerator / k;
            if (avg > avg_max) {
                avg_max = avg;
            }
            i++;
        }
        return avg_max;
    }
};
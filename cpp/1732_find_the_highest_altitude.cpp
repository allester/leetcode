/*
https://leetcode.com/problems/find-the-highest-altitude/submissions/1121316704/?envType=study-plan-v2&envId=leetcode-75
*/

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int sum = 0;
        int highest = 0;
        for (const int& x : gain) {
            sum += x;
            if (sum > highest) {
                highest = sum;
            }
        }
        return highest;
    }
};
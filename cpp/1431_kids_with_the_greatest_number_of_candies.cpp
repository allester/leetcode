/*
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1108578573/
*/


class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int MAX = * max_element(candies.begin(), candies.end());
        vector<bool> res;
        for (int n : candies) {
            if (n + extraCandies >= MAX) {
                res.push_back(true);
            } else {
                res.push_back(false);
            }
        }
        return res;
    }
};
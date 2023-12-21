/*
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/submissions/1125436167/
*/

class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> xs;
        int n = points.size();
        int ans = 0;
        for (int i = 0; i < n; i++) xs.push_back(points[i][0]);
        sort(xs.begin(), xs.end());
        for (int i = 1; i < n; i++) ans = max(ans, xs[i] - xs[i-1]);
        return ans;
    }
};
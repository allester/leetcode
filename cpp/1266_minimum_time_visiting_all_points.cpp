/*
https://leetcode.com/problems/minimum-time-visiting-all-points/submissions/1111925928/?envType=daily-question&envId=2023-12-03
*/

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int time = 0;
        for (int i = 1; i < points.size(); i++) {
            int x1 = points[i-1][0];
            int y1 = points[i-1][1];
            int x2 = points[i][0];
            int y2 = points[i][1];
            int dx = abs(x2 - x1);
            int dy = abs(y2 - y1);
            time += max(dx, dy);
        }
        return time;
    }
};
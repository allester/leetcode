/*
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/submissions/1119776697/
*/

class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> rows(m, 0), cols(n, 0);
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                rows[row] += grid[row][col];
                cols[col] += grid[row][col];
            }
        }
        vector<vector<int>> diff(m, vector<int> (n));
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                diff[row][col] = 2 * (rows[row] + cols[col]) - (m + n);
            }
        }
        return diff;
    }
};
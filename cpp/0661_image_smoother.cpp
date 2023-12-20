/*
https://leetcode.com/problems/image-smoother/submissions/1124503608/
*/

class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int n = img.size(), m = img[0].size();
        vector<vector<int>> res(n, vector<int> (m, 0));
        
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                int sum = 0, count = 0;
                for (int i = -1; i <= 1; i++) {
                    for (int j = -1; j <= 1; j++) {
                        if (row + i >= 0 && row + i < n && col + j >=0 && col + j < m) {
                            sum += img[row + i][col + j];
                            count++;
                        }
                    }
                }
                res[row][col] = sum / count;
            }
        }
        return res;
    }
};
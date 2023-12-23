/*
https://leetcode.com/problems/maximum-score-after-splitting-a-string/submissions/1125997182/
*/

class Solution {
public:
    int maxScore(string s) {
        const int n = s.size();
        int ones = 0;
        for (int i = 1; i < n; i++) if (s[i] == '1') ones++;
        int zeros = s[0]=='1'?0:1;
        int ans = ones + zeros;
        for (int i = 1; i < n-1; i++) {
            if (s[i] == '0') zeros++;
            else ones--;
            ans = max(ans, zeros + ones);
        }
        return ans;
    }
};
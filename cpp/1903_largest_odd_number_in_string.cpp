/*
https://leetcode.com/problems/largest-odd-number-in-string/submissions/1114563312/
*/

class Solution {
public:
    string largestOddNumber(string num) {
        int end = -1;
        for (int i = num.length() - 1; i > -1; i--) {
            if ((num[i] - 0) % 2 != 0) {
                end = i;
                break;
            }
        }
        if (end == -1) {
            return "";
        }
        return num.substr(0, end + 1);
    }
};
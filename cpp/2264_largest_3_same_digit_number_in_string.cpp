/*
https://leetcode.com/problems/largest-3-same-digit-number-in-string/submissions/1112568249/?envType=daily-question&envId=2023-12-04
*/

class Solution {
public:
    string largestGoodInteger(string num) {
        string res = "";
        for (int i = 0; i < num.size() - 2; i++) {
            string str = num.substr(i, 3);
            if (str[0] != str[1] || str[0] != str[2]) {
                continue;
            }
            if (res.compare(str) < 0) {
                res = str;
            }
        }
        return res;
    }
};
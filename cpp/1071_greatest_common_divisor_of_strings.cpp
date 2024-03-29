/*
https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/
*/

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) {
            return "";
        }
        int i = gcd(str1.size(), str2.size());
        return str1.substr(0, i);
    }
};
/*
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/submissions/1127070043/
*/

class Solution {
public:
    int minOperations(string s) {
        const int n = s.length();
        int a = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0 && s[i] == '0') a++;
            if (i % 2 == 1 && s[i] == '1') a++;
        }
        int b = s.length() - a;
        return min(a, b);
    }
};
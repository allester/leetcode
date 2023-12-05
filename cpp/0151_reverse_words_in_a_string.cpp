/*
https://leetcode.com/problems/reverse-words-in-a-string/submissions/1113076004/
*/

class Solution {
public:
    string reverseWords(string s) {
        int i = s.length() - 1;
        int p1, p2;
        string result = "";
        while (i >= 0) {
            while (i >= 0 && s[i] == ' ') i--;
            p2 = i;

            while(i >= 0 && s[i] != ' ') i--;
            p1 = i + 1;

            result += s.substr(p1, p2 - p1 + 1);
            result += " ";
        }
        while (!result.empty() && result.back() == ' ') {
            result.pop_back();
        }
        return result;
    }
};
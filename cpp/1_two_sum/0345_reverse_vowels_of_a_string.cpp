/*
https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1108616276/
*/

class Solution {
public:
    string reverseVowels(string s) {
        string stack = "";
        string vowels = "aeiouAEIOU";
        for (auto c : s) {
            if (vowels.find(c) != -1) {
                stack.push_back(c);
            }
        }
        for (int i = 0; i < s.size(); i++) {
            if (vowels.find(s[i]) != -1) {
                s[i] = stack.back();
                stack.pop_back();
            }
        }
        return s;
    }
};
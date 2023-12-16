/*
https://leetcode.com/problems/valid-anagram/submissions/1121223896/
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> mp;
        for (const char& c : s) {
            mp[c]++;
        }
        for (const char& c : t) {
            if (--mp[c] < 0) return false;
        }
        return true;
    }
};
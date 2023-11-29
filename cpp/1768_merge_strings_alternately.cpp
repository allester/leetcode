/*
https://leetcode.com/problems/merge-strings-alternately/submissions/1108567638/
*/

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";
        int i = 0;
        int j = 0;
        int n = word1.size();
        int m = word2.size();
        while (i < n || j < m) {
            if (i < n) {
                result.push_back(word1[i]);
                i++;
            }
            if (j < m) {
                result.push_back(word2[j]);
                j++;
            }
        }
        return result;
    }
};
/*
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/submissions/1111158138/
*/

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int charCount[26] = {};
        int result = 0;
        for (char& c : chars) {
            charCount[c - 'a'] += 1;
        }
        for (string& word: words) {
            int tempCount[26] = {};
            bool isValid = true;
            for (char& c: word) {
                tempCount[c - 'a'] += 1;
            }
            for (int i = 0; i < 26; i++) {
                if (charCount[i] < tempCount[i]) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                result += word.size();
            }
        }
        return result;
    }
};
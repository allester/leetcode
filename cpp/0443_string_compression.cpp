/*
https://leetcode.com/problems/string-compression/submissions/1113943347/
*/

class Solution {
public:
    int compress(vector<char>& chars) {
      string s = "";
      char c = chars[0];
      int count = 1;
      for (int i = 1; i < chars.size(); i++) {
        if (chars[i] == c) {
          count++;
        } else {
          s += c;
          c = chars[i];
          if (count > 1) {
            s += to_string(count);
          }
          count = 1;
        }
      }
      s += c;
      if (count > 1) {
        s += to_string(count);
      }
      chars.clear();
      for (const char& x : s) {
        chars.push_back(x);
      }
      return chars.size();
    }
};
/*
https://leetcode.com/problems/path-crossing/submissions/1126909520/
*/

class Solution {
public:
    bool isPathCrossing(string path) {
        unordered_set<string> visited {"0,0"};
        int x = 0, y = 0;
        string coord;
        for (const char& c : path) {
            if (c == 'N') y++;
            else if (c == 'E') x++;
            else if (c == 'S') y--;
            else x--;
            coord = to_string(x) + "," + to_string(y);
            if (visited.count(coord)) return true;
            visited.insert(coord);
        }
        return false;
    }
};
/*
https://leetcode.com/problems/destination-city/submissions/1120482896/
*/

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        const int n = paths.size();
        unordered_set<string> destinations;
        for (vector<string>& path : paths) destinations.insert(path[1]);
        for (vector<string>& path : paths) destinations.erase(path[0]);
        return *destinations.begin();
    }
};
/*
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/submissions/1125458909/
*/

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        const int n = spells.size(), m = potions.size();
        vector<int> ans(spells.size(), 0);
        for (int i = 0; i < n; i++) {
            int l = 0;
            int r = m - 1;
            int j;
            while (l <= r) {
                j = l + (r - l) / 2;
                if (long(spells[i]) * potions[j] >= success) {
                    r = j - 1;
                } else {
                    l = j + 1;
                }
            }
            ans[i] = m - l;
        }
        return ans;
    }
};
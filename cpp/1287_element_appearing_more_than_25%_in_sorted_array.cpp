/*
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/submissions/1117429776/
*/

class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        const int n = arr.size();
        const int m = n / 4;
        if (n == 1) return arr[0];

        int count = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] == arr[i-1]) {
                count++;
                if (count > m) {
                    return arr[i];
                }
            } else {
                count = 1;
            }
        }
        return 0;
    }
};
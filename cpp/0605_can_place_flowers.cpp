/*
https://leetcode.com/problems/can-place-flowers/submissions/1108602995/
*/

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size(); 
        if (n == 0) { return true; }
        for (int i = 0;  i < len; i++) {
            if ((i == 0 || flowerbed[i - 1] == 0) && (i == len - 1 || flowerbed[i + 1] == 0) && flowerbed[i] == 0) {
                flowerbed[i] = 1;
                n--;
            }
            if (n == 0) {
                return true;
            }
        }
        return false;
    }
};
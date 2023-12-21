/*
https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1125452468/
*/

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int l = 1;
        int r = n;
        int i, g;
        while (l <= r) {
            i = l + (r - l) / 2;
            g = guess(i);
            if (g == -1) {
                r = i - 1;
            } else if (g == 1) {
                l = i + 1;
            } else {
                return i;
            }
        }
        return -1;
    }
};
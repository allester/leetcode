/*
https://leetcode.com/problems/count-of-matches-in-tournament/submissions/1112571224/
*/

class Solution {
public:
    int numberOfMatches(int n) {
        int result = 0;
        while (n != 1) {
            if (n % 2 != 0) {
                result++;
                n--;
            }
            n /= 2;
            result += n;
        }
        return result;
    }
};
/*
https://leetcode.com/problems/average-waiting-time/submissions/1315524395/?envType=daily-question&envId=2024-07-09
*/
class Solution {
    public double averageWaitingTime(int[][] customers) {
        int currentTime = customers[0][0];
        double totalWaitTime = 0;
        for (int i = 0; i < customers.length; i++) {
            if (currentTime < customers[i][0])
                currentTime = customers[i][0];
            totalWaitTime += currentTime - customers[i][0] + customers[i][1];
            currentTime += customers[i][1];
        }
        return totalWaitTime / customers.length;
    }
}
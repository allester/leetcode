import java.lang.Math;

class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;
        int max = -1;
        while (i < j) {
            max = Math.max(Math.min(height[i], height[j]) * (j - i), max);
            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }
        return max;
    }
}
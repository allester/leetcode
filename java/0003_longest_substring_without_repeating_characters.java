/*
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1287298218/
 */

import java.util.Set;
import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<> ();
        int max = 0;
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            while (set.contains(c)) {
                set.remove(s.charAt(j++));
            }
            set.add(c);
            max = Math.max(max, set.size());
        }
        return max;
    }
}
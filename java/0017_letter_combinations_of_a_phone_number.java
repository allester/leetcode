/*
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1287352225/
 */

import java.util.ArrayList;
import java.util.List;
import java.lang.StringBuilder;


class Solution {
    List<String> combinations = new ArrayList<> ();
    String[] map = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    String digits;
    int N;

    public List<String> letterCombinations(String digits) {
        N = digits.length();
        this.digits = digits;
        if (N == 0) {
            return combinations;
        }
        dfs(0, new StringBuilder());
        return combinations;
    }

    void dfs(int i, StringBuilder combination) {
        if (i == N) {
            combinations.add(combination.toString());
            return;
        }
        String letters = map[digits.charAt(i) - '0'];
        for (int j = 0; j < letters.length(); j++) {
            char letter = letters.charAt(j);
            combination.append(letter);
            dfs(i + 1, combination);
            combination.deleteCharAt(combination.length() - 1);
        }


    }
}
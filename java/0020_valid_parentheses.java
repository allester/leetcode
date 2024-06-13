/*
 * https://leetcode.com/problems/valid-parentheses/submissions/1286763643/
 */

class Solution {
    public boolean isValid(String s) {
        int N = s.length();
        int top = -1;
        char[] stack = new char[N];
        for (int i = 0; i < N; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack[++top] = ')';
            } else if (c == '{') {
                stack[++top] = '}';
            } else if (c == '[') {
                stack[++top] = ']';
            } else if (top != -1 && stack[top] == c) {
                top--;
            } else {
                return false;
            }
        }
        return top == -1;
    }
}
//https://leetcode.com/problems/valid-parentheses/submissions/1037086407/

impl Solution {
    pub fn is_valid(s: String) -> bool {
        if s.len() % 2 == 1 { return false }

        let mut stack = vec![];
        for c in s.chars() {
            match c {
                '(' => stack.push(')'),
                '{' => stack.push('}'),
                '[' => stack.push(']'),
                ')' | '}' | ']' if Some(c) != stack.pop() => return false ,
                _ => ()
            }
        }
        stack.is_empty()
    }
}
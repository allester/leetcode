/*
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/submissions/1110437668/
*/

impl Solution {
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        let s1: String = word1.iter().map(|s| s.chars()).flatten().collect();
        let s2: String = word2.iter().map(|s| s.chars()).flatten().collect();
        s1 == s2
    }
}
'''
https://leetcode.com/problems/merge-strings-alternately/submissions/1109084194/?envType=study-plan-v2&envId=leetcode-75
'''

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::with_capacity(word1.len() + word2.len());
        
        let mut chars1 = word1.chars();
        let mut chars2 = word2.chars();

        for i in 0..word1.len().max(word2.len()) {
            match chars1.next() {
                Some(char) => { result.push(char); },
                _ => {}
            }
            match chars2.next() {
                Some(char) => { result.push(char); },
                _ => {}
            }
        }
        result
    }
}
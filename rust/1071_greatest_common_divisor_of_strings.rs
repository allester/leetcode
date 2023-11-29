'''
https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1109099818/
'''

impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        if format!("{}{}", str1, str2) == format!("{}{}", str2, str1) {
            let i = Solution::gcd(str1.len(), str2.len());
            return String::from(&str1[..i]);
        }
        String::new()
    }
    fn gcd(a: usize, b: usize) -> usize {
        if b == 0 {
            return a;
        }
        Solution::gcd(b, a % b)
    }
}
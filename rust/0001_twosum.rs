//https://leetcode.com/problems/two-sum/submissions/909162045/

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut d: HashMap<i32, usize> = HashMap::with_capacity(nums.len());

        for (i, num) in nums.into_iter().enumerate() {
            let x = target - num;
            match(d.get(&x)) {
                Some(&index) => {
                    return vec![index as i32, i as i32];
                }
                None => {
                    d.insert(num, i);
                }
            }
        }
        return vec![];
    }
}
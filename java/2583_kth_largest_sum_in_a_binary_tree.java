/*
 * https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/submissions/1430619136/?envType=daily-question&envId=2024-10-22
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public long kthLargestLevelSum(TreeNode root, int k) {
        // initialize
        PriorityQueue<Long> pq = new PriorityQueue<>(k);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        // bfs by level
        while (!q.isEmpty()) {
            int m = q.size();
            long sum = 0;
            for (int i = 0; i < m; i++) {
                TreeNode node = q.poll();
                sum += node.val;
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            pq.add(sum * -1);
        }

        // get kth largest
        if (k > pq.size())
            return -1;
        long ans = 0;
        for (int i = 0; i < k; i++)
            ans = pq.poll();
        return ans * -1;
    }
}
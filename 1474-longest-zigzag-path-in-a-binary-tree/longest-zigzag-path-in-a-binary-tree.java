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
    public int longestZigZag(TreeNode root) {
        if (root == null) {
            return 0;
        }

        return Math.max(dfs(root.left, "right", 1), dfs(root.right, "left", 1));
    }

    private int dfs(TreeNode node, String direction, int length) {
        if (node == null) {
            return length - 1;
        }

        if (direction.equals("left")) {
            return Math.max(dfs(node.left, "right", length + 1), dfs(node.right, "left", 1));
        } else {
            return Math.max(dfs(node.right, "left", length + 1), dfs(node.left, "right", 1));
        }
    }
}
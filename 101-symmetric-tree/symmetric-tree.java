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
    public boolean isSymmetric(TreeNode root) {
        if(root == null)
        {
            return true;
        }

        return helper(root.left, root.right);
    }

    public boolean helper(TreeNode one, TreeNode two)
    {
        if(one == null && two == null)
        {
            return true;
        }

        if(one == null || two == null)
        {
            return false;
        }

        if(one.val != two.val)
        {
            return false;
        }

        return helper(one.left, two.right) && helper(one.right,two.left);
    }
}
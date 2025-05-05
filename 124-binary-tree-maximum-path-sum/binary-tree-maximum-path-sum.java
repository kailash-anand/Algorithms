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
class Solution 
{
    public int result;

    public int maxPathSum(TreeNode root) 
    {
        result = root.val;
        computeMax(root);
        return result;
    }

    public int computeMax(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        int leftMax = Math.max(computeMax(root.left), 0);
        int rightMax = Math.max(computeMax(root.right), 0);

        int newMax = root.val + leftMax + rightMax;
        if (newMax > result)
        {
            result = newMax;
        }

        return root.val + Math.max(leftMax, rightMax);
    }
}
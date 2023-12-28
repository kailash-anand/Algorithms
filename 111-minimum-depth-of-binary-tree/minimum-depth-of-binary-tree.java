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

    public int minimumDepth(TreeNode root)
    {
        if(root == null)
        {
            return 0;
        }

        int temp = 1 + minimumDepth(root.left);
        int temp2 = 1 + minimumDepth(root.right);

        if(temp != 1 && temp2 != 1)
          return Math.min(temp,temp2);
        else
          return Math.max(temp,temp2);  
    }

    public int minDepth(TreeNode root) {

        if(root == null) return 0;
        if(root.left == null && root.right == null)
        { return 1; }

        return minimumDepth(root);
    }
}
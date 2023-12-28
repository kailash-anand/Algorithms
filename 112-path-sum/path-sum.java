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

    public boolean sum(TreeNode root, int sum, int targetSum,int ans)
    {
        if(((sum+root.val) == targetSum) && isLeaf(root))
        { return true; }
        boolean left = false;
        if(root.left != null)
        { left = sum(root.left,sum+root.val,targetSum,ans); }

        if(root.right != null)
        { return left || sum(root.right,sum+root.val,targetSum,ans); }
        else return left;
    }

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root != null)
        { 
            return sum(root,0,targetSum,-2021); 
        }
        // else
        // { return false;}
        return false;
    }

    public boolean isLeaf(TreeNode root)
    {
        return root.left == null && root.right == null;
    }
}
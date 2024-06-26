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
    public int goodNodes(TreeNode root) 
    {
        return count(root, root.val);
    }

    public int count(TreeNode node, int maxBranchValue)
    {
        if(node == null)
        {
            return 0;
        }

        if(node.val >= maxBranchValue)
        {
            return count(node.left, node.val) + count(node.right, node.val) + 1;
        }
        else
        {
            return count(node.left, maxBranchValue) + count(node.right, maxBranchValue);
        }
    }
}
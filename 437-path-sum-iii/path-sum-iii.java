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
    public int pathSum(TreeNode root, int targetSum) {
        if(root == null)
        {
            return 0;
        }

        int paths = countPaths(root, 0, targetSum);
        return paths + pathSum(root.left,targetSum) + pathSum(root.right,targetSum);
    }

    public int countPaths(TreeNode node, long currentSum, int targetSum)
    {
        if(node == null)
        {
            return 0;
        }

        currentSum += node.val;
        int paths = 0;
        if(currentSum == targetSum)
        {
            paths++;
        }

        paths += countPaths(node.left, currentSum, targetSum);  
        paths += countPaths(node.right, currentSum, targetSum);

        return paths;
    }

}
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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves1 = new ArrayList<>();
        List<Integer> leaves2 = new ArrayList<>();

        collectLeaves(root1, leaves1);
        collectLeaves(root2, leaves2);

        if(leaves1.size() != leaves2.size())
        {
            return false;
        }

        for(int i = 0; i < leaves1.size() ; i++)
        {
            if(leaves1.get(i) != leaves2.get(i))
            {
                return false;
            }
        }

        return true;
    }

    public void collectLeaves(TreeNode root, List<Integer> leaves)
    {
        if(root.left != null)
        {
            collectLeaves(root.left, leaves);
        }

        if(root.right != null)
        {
            collectLeaves(root.right, leaves);
        }

        if(root.left == null && root.right == null)
        {
            leaves.add(root.val);
        }
    }
}
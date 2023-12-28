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

    public void preorder(TreeNode root, List list)
    {
        list.add(root.val);

        if(root.left != null)
        { preorder(root.left,list); }

        if(root.right != null)
        { preorder(root.right,list); }
    }

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList();

        if(root == null)
        { return list; }

        preorder(root,list);
        return list;
    }
}
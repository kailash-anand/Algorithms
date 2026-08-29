# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def traverse_tree(node, curr_sum, curr_path):
            if node == None:
                return

            new_sum = curr_sum + node.val
            curr_path.append(node.val)

            if node.left == None and node.right == None:
                if new_sum == targetSum:
                    result.append(curr_path)
                return

            traverse_tree(node.left, new_sum, curr_path.copy())
            traverse_tree(node.right, new_sum, curr_path.copy())


        traverse_tree(root, 0, [])

        return result
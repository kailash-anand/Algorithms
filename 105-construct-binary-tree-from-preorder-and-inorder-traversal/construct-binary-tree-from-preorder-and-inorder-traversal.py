# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        root = None
        self.pIndex = 0
        
        def helper(left, right):
            if self.pIndex < len(preorder):
                findIndex = inorder_map[preorder[self.pIndex]]
                 
                if findIndex >= left and findIndex <= right:
                    node = TreeNode(preorder[self.pIndex])
                    self.pIndex += 1
                    node.left = helper(left, findIndex)
                    node.right = helper(findIndex + 1, right)
                    return node

                return None

        root = helper(0 , len(inorder))
        return root
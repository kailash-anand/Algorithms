# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inorder(root: Optional[TreeNode]) -> None:
            if root != None:
                inorder(root.left)

                if self.prev is not None:
                    self.min_diff = min(self.min_diff, root.val - self.prev) 
                self.prev = root.val
                
                inorder(root.right)

        
        inorder(root)

        return self.min_diff

    

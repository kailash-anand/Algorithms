# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        self.pIndex = 0
        
        def helper(inorder):
            if self.pIndex < len(preorder):
                findIndex = -1
                for i in range(len(inorder)):
                    if inorder[i] == preorder[self.pIndex]:
                        findIndex = i
                        break

                if findIndex != -1:
                    node = TreeNode(preorder[self.pIndex])
                    self.pIndex += 1
                    node.left = helper(inorder[:findIndex])
                    node.right = helper(inorder[findIndex + 1:])
                    return node

                return None

        root = helper(inorder)
        return root
            

                

                

            

            


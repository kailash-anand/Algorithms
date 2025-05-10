# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nodes = list()

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.collectNodes(root)
        self.nodes.sort()
        min_diff = self.nodes[1] - self.nodes[0]

        for i in range(len(self.nodes) - 1):
            if (self.nodes[i + 1] - self.nodes[i]) < min_diff:
                min_diff =  self.nodes[i + 1] - self.nodes[i]

        self.nodes.clear()
        return min_diff

    def collectNodes(self, root: Optional[TreeNode]) -> None:
        if root != None:
            self.nodes.append(root.val)

            self.collectNodes(root.left)
            self.collectNodes(root.right)

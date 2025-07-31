"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def __init__(self):
        self.old = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        if node in self.old:
            return self.old[node]

        newNode = Node(node.val)
        self.old[node] = newNode
       
        for neighbor in node.neighbors:
            newNeighbor = self.cloneGraph(neighbor)
            newNode.neighbors.append(newNeighbor)

        return newNode    
"""
    File: 133.py
    Title: Clone Graph
    Difficulty: Medium
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        nodes = [None] * (100 + 1)

        def dfs(n):
            copy = Node(n.val)
            nodes[n.val] = copy

            for neighbor in n.neighbors:
                if nodes[neighbor.val] is None:
                    dfs(neighbor)
                copy.neighbors.append(nodes[neighbor.val])

        dfs(node)

        return nodes[node.val]

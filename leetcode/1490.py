"""
    File: 1490.py
    Title: Clone N-ary Tree
    Difficulty: Medium
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: "Node") -> "Node":
        if root is None:
            return None

        children = []
        for child in root.children:
            clone = self.cloneTree(child)
            children.append(clone)
        return Node(root.val, children)

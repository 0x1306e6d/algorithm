"""
    File: 1650.py
    Title: Lowest Common Ancestor of a Binary Tree III
    Difficulty: Medium
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        path = {}

        while p:
            path[p.val] = p
            p = p.parent

        while q:
            if q.val in path:
                return q
            q = q.parent

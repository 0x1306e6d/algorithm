"""
    File: 1522.py
    Title: Diameter of N-Ary Tree
    Difficulty: Medium
"""

from heapq import heappop, heappush


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: "Node") -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0

        def solve(node):
            ans = 0
            h = []
            for child in node.children:
                path = solve(child)
                heappush(h, -path)
            if len(h) == 0:
                return 0
            first = -heappop(h) + 1
            if h:
                second = -heappop(h) + 1
                self.ans = max(self.ans, first + second)
            else:
                self.ans = max(self.ans, first)
            return first

        solve(root)

        return self.ans

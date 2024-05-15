"""
    File: 427.py
    Title: Construct Quad Tree
    Difficulty: Medium
"""

from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        n = len(grid)

        def _construct(x, y, side):
            if side == 1:
                return Node(grid[y][x] == 1, True, None, None, None, None)

            mid = side // 2
            topLeft = _construct(x, y, mid)
            topRight = _construct(x + mid, y, mid)
            bottomLeft = _construct(x, y + mid, mid)
            bottomRight = _construct(x + mid, y + mid, mid)
            if (
                topLeft.isLeaf
                and topRight.isLeaf
                and bottomLeft.isLeaf
                and bottomRight.isLeaf
            ):
                if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                    return Node(topLeft.val, True, None, None, None, None)
            return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)

        return _construct(0, 0, n)

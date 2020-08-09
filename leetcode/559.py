"""
    File: 559.py
    Title: Maximum Depth of N-ary Tree
    Difficulty: Easy
    URL: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""

import unittest

from typing import List


class Node:
    def __init__(self, val: int, children: List['Node']):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root)

    def dfs(self, node: 'Node') -> int:
        if node:
            if node.children:
                max_depth = 0
                for child in node.children:
                    max_depth = max(max_depth, self.dfs(child))
                return 1 + max_depth
            else:
                return 1
        else:
            return 0


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = Node(1,
                    [Node(2, []),
                     Node(3, [Node(5, []), Node(6, [])]),
                     Node(4, [])])
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.maxDepth(root), output)

    def test_example2(self):
        # Input
        root = Node(1,
                    [Node(2, []),
                     Node(3, [Node(6, []), Node(7, [Node(11, [Node(15, [])])])]),
                     Node(4, [Node(8, [Node(12, [])])]),
                     Node(5, [Node(9, [Node(13, []), Node(10, [])])])])
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.maxDepth(root), output)


if __name__ == "__main__":
    unittest.main()

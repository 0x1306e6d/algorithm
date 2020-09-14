"""
    File: 100.py
    Title: Same Tree
    Difficulty: Easy
    URL: https://leetcode.com/problems/same-tree/
"""

import unittest

from typing import List


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: "TreeNode" = None,
                 right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.get_nodes(p) == self.get_nodes(q)

    def get_nodes(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        nodes = [root.val]
        if root.left is not None:
            nodes += self.get_nodes(root.left)
        else:
            nodes.append(None)
        if root.right is not None:
            nodes += self.get_nodes(root.right)
        else:
            nodes.append(None)
        return nodes


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isSameTree(p, q), output)

    def test_example2(self):
        # Input
        p = TreeNode(1, TreeNode(2), None)
        q = TreeNode(1, None, TreeNode(2))
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isSameTree(p, q), output)

    def test_example3(self):
        # Input
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isSameTree(p, q), output)


if __name__ == "__main__":
    unittest.main()

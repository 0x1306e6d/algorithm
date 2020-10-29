"""
    File: 144.py
    Title: Binary Tree Preorder Traversal
    Difficulty: Medium
    URL: https://leetcode.com/problems/binary-tree-preorder-traversal/
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        preorder = [root.val]
        if root.left is not None:
            preorder += self.preorderTraversal(root.left)
        if root.right is not None:
            preorder += self.preorderTraversal(root.right)
        return preorder


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        # Output
        output = [1, 2, 3]

        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), output)

    def test_example2(self):
        # Input
        root = None
        # Output
        output = []

        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), output)

    def test_example3(self):
        # Input
        root = TreeNode(1)
        # Output
        output = [1]

        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), output)

    def test_example4(self):
        # Input
        root = TreeNode(1, TreeNode(2))
        # Output
        output = [1, 2]

        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), output)

    def test_example5(self):
        # Input
        root = TreeNode(1, None, TreeNode(2))
        # Output
        output = [1, 2]

        solution = Solution()
        self.assertEqual(solution.preorderTraversal(root), output)


if __name__ == "__main__":
    unittest.main()

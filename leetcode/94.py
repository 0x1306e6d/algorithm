"""
    File: 94.py
    Title: Binary Tree Inorder Traversal
    Difficulty: Medium
    URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

import unittest

from typing import List


class TreeNode:
    def __init__(self,
                 val: int,
                 left: "TreeNode" = None,
                 right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        traversal = []
        if root.left is not None:
            traversal += self.inorderTraversal(root.left)
        traversal.append(root.val)
        if root.right is not None:
            traversal += self.inorderTraversal(root.right)
        return traversal


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        # Output
        output = [1, 3, 2]

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), output)


if __name__ == "__main__":
    unittest.main()

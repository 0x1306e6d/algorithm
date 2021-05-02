"""
    File: 98.py
    Title: Validate Binary Search Tree
    Difficulty: Medium
    URL: https://leetcode.com/problems/validate-binary-search-tree/
"""

import sys
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
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node: TreeNode, minimum: int, maximum: int) -> bool:
            if node is None:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False
            if not validate(node.left, minimum, node.val):
                return False
            return validate(node.right, node.val, maximum)
        return validate(root, -sys.maxsize, sys.maxsize)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isValidBST(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(5,
                        TreeNode(1),
                        TreeNode(4, TreeNode(3), TreeNode(6)))
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isValidBST(root), output)


if __name__ == "__main__":
    unittest.main()

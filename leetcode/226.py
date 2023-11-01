"""
    File: 226.py
    Title: Invert Binary Tree
    Difficulty: Easy
    URL: https://leetcode.com/problems/invert-binary-tree/description/
"""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, o) -> bool:
        return self.val == o.val and \
            self.left == o.left and self.right == o.right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        return TreeNode(root.val,
                        self.invertTree(root.right),
                        self.invertTree(root.left))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(4,
                        TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(7, TreeNode(6), TreeNode(9)))
        # Output
        output = TreeNode(4,
                          TreeNode(7, TreeNode(9), TreeNode(6)),
                          TreeNode(2, TreeNode(3), TreeNode(1)))

        solution = Solution()
        self.assertEqual(solution.invertTree(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        # Output
        output = TreeNode(2, TreeNode(3), TreeNode(1))

        solution = Solution()
        self.assertEqual(solution.invertTree(root), output)

    def test_example3(self):
        # Input
        root = None
        # Output
        output = None

        solution = Solution()
        self.assertEqual(solution.invertTree(root), output)


if __name__ == "__main__":
    unittest.main()

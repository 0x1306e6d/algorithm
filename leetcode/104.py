"""
    File: 104.py
    Title: Maximum Depth of Binary Tree
    Difficulty: Easy
    URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

import unittest


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: "TreeNode" = None,
                 right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 1
        if root.left is not None:
            depth = max(depth, 1 + self.maxDepth(root.left))
        if root.right is not None:
            depth = max(depth, 1 + self.maxDepth(root.right))
        return depth


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(3,
                        TreeNode(9),
                        TreeNode(20, TreeNode(15), TreeNode(7)))
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.maxDepth(root), output)


if __name__ == "__main__":
    unittest.main()

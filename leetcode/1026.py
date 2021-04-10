"""
    File: 1026.py
    Title: Maximum Difference Between Node and Ancestor
    Difficulty: Medium
    URL: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
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
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, min_until: int, max_until: int):
            diff = max(abs(min_until - node.val), abs(max_until - node.val))
            next_min = min(min_until, node.val)
            next_max = max(max_until, node.val)
            if node.left is not None:
                diff = max(diff, dfs(node.left, next_min, next_max))
            if node.right is not None:
                diff = max(diff, dfs(node.right, next_min, next_max))
            return diff

        return dfs(root, root.val, root.val)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(8,
                        TreeNode(3,
                                 TreeNode(1),
                                 TreeNode(6,
                                          TreeNode(4),
                                          TreeNode(7))),
                        TreeNode(10,
                                 None,
                                 TreeNode(14,
                                          TreeNode(13))))
        # Output
        output = 7

        solution = Solution()
        self.assertEqual(solution.maxAncestorDiff(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(1,
                        None,
                        TreeNode(2,
                                 None,
                                 TreeNode(0,
                                          TreeNode(3))))
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.maxAncestorDiff(root), output)


if __name__ == "__main__":
    unittest.main()

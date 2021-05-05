"""
    File: 337.py
    Title: House Robber III
    Difficulty: Medium
    URL: https://leetcode.com/problems/house-robber-iii/
"""

import unittest

from collections import deque
from typing import Tuple


class TreeNode:
    def __init__(self,
                 val: int,
                 left: "TreeNode" = None,
                 right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def do_rob(node: TreeNode) -> Tuple[int, int]:
            robbing = node.val
            not_robbing = 0

            if node.left is not None:
                left_robbed, left_not_robbed = do_rob(node.left)
                robbing += left_not_robbed
                not_robbing += max(left_robbed, left_not_robbed)

            if node.right is not None:
                right_robbed, right_not_robbed = do_rob(node.right)
                robbing += right_not_robbed
                not_robbing += max(right_robbed, right_not_robbed)

            return (robbing, not_robbing)

        return max(do_rob(root))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(3,
                        TreeNode(2, None, TreeNode(3)),
                        TreeNode(3, None, TreeNode(1)))
        # Output
        output = 7

        solution = Solution()
        self.assertEqual(solution.rob(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(3,
                        TreeNode(4, TreeNode(1), TreeNode(3)),
                        TreeNode(5, None, TreeNode(1)))
        # Output
        output = 9

        solution = Solution()
        self.assertEqual(solution.rob(root), output)


if __name__ == "__main__":
    unittest.main()

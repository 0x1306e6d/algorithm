"""
    File: 129.py
    Title: Sum Root to Leaf Numbers
    Difficulty: Medium
    URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/
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

    def __eq__(self, o) -> bool:
        return self.val == o.val and \
            self.left == o.left and self.right == o.right

    def __repr__(self) -> str:
        return "{}".format(self.val)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val

        answer = 0
        if root.left is not None:
            answer += self.dfs(root.left, root.val)
        if root.right is not None:
            answer += self.dfs(root.right, root.val)
        return answer

    def dfs(self, root: TreeNode, number: int) -> int:
        base = number * 10 + root.val

        if root.left is None and root.right is None:
            return base

        sum_numbers = 0
        if root.left is not None:
            sum_numbers += self.dfs(root.left, base)
        if root.right is not None:
            sum_numbers += self.dfs(root.right, base)
        return sum_numbers


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        # Output
        output = 25

        solution = Solution()
        self.assertEqual(solution.sumNumbers(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
        # Output
        output = 1026

        solution = Solution()
        self.assertEqual(solution.sumNumbers(root), output)


if __name__ == "__main__":
    unittest.main()

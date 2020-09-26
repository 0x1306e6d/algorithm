"""
    File: 1315.py
    Title: Sum of Nodes with Even-Valued Grandparent
    Difficulty: Medium
    URL: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
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


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.traverse(None, root)

    def traverse(self, grandparent: TreeNode, parent: TreeNode) -> int:
        if grandparent is None:
            is_even = False
        else:
            is_even = (grandparent.val % 2) == 0

        sum_nodes = 0

        if parent.left is not None:
            if is_even:
                sum_nodes += parent.left.val
            sum_nodes += self.traverse(parent, parent.left)

        if parent.right is not None:
            if is_even:
                sum_nodes += parent.right.val
            sum_nodes += self.traverse(parent, parent.right)

        return sum_nodes


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(6,
                        TreeNode(7,
                                 TreeNode(2, TreeNode(9)),
                                 TreeNode(7, TreeNode(1), TreeNode(4))),
                        TreeNode(8,
                                 TreeNode(1),
                                 TreeNode(3, None, TreeNode(5))))
        # Output
        output = 18

        solution = Solution()
        self.assertEqual(solution.sumEvenGrandparent(root), output)


if __name__ == "__main__":
    unittest.main()

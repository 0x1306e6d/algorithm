"""
    File: 404.py
    Title: Sum of Left Leaves
    Difficulty: Easy
    URL: https://leetcode.com/problems/sum-of-left-leaves/
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
    def sumOfLeftLeaves(self, root: TreeNode, left: bool = False) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val if left else 0

        sum_of_left_leaves = 0
        if root.left is not None:
            sum_of_left_leaves += self.sumOfLeftLeaves(root.left, True)
        if root.right is not None:
            sum_of_left_leaves += self.sumOfLeftLeaves(root.right, False)
        return sum_of_left_leaves


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(3,
                        TreeNode(9),
                        TreeNode(20, TreeNode(15), TreeNode(7)))
        # Output
        output = 24

        solution = Solution()
        self.assertEqual(solution.sumOfLeftLeaves(root), output)


if __name__ == "__main__":
    unittest.main()

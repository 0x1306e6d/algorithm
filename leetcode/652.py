"""
    File: 652.py
    Title: Find Duplicate Subtrees
    Difficulty: Medium
    URL: https://leetcode.com/problems/find-duplicate-subtrees/
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
        if o is None:
            return False
        if self.val != o.val:
            return False
        return (self.left == o.left) and (self.right == o.right)


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ans = []

        memo = {}

        def traverse(node: TreeNode) -> str:
            key = f"{node.val}"

            if node.left is None:
                key += ", None"
            else:
                key += f", {traverse(node.left)}"

            if node.right is None:
                key += ", None"
            else:
                key += f", {traverse(node.right)}"

            if key in memo:
                if memo[key] == 1:
                    ans.append(node)
                memo[key] += 1
            else:
                memo[key] = 1

            return key

        traverse(root)

        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(1,
                        TreeNode(2, TreeNode(4)),
                        TreeNode(3,
                                 TreeNode(2, TreeNode(4)),
                                 TreeNode(4)))
        # Output
        output = [TreeNode(4), TreeNode(2, TreeNode(4))]

        solution = Solution()
        self.assertEqual(solution.findDuplicateSubtrees(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(1, TreeNode(1), TreeNode(1))
        # Output
        output = [TreeNode(1)]

        solution = Solution()
        self.assertEqual(solution.findDuplicateSubtrees(root), output)

    def test_example3(self):
        # Input
        root = TreeNode(1,
                        TreeNode(2, TreeNode(3)),
                        TreeNode(2, TreeNode(3)))
        # Output
        output = [TreeNode(3), TreeNode(2, TreeNode(3))]

        solution = Solution()
        self.assertEqual(solution.findDuplicateSubtrees(root), output)


if __name__ == "__main__":
    unittest.main()

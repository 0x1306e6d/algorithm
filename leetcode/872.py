"""
    File: 872.py
    Title: Leaf-Similar Trees
    Difficulty: Easy
    URL: https://leetcode.com/problems/leaf-similar-trees/
"""

import unittest

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaves_of(root1) == self.leaves_of(root2)

    def leaves_of(self, root: TreeNode) -> List[int]:
        if (root.left is None) and (root.right is None):
            return [root.val]

        leaves = []
        if root.left is not None:
            leaves += self.leaves_of(root.left)
        if root.right is not None:
            leaves += self.leaves_of(root.right)
        return leaves


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root1 = TreeNode(3,
                         TreeNode(5,
                                  TreeNode(6),
                                  TreeNode(2, TreeNode(7), TreeNode(4))),
                         TreeNode(1, TreeNode(9), TreeNode(8)))
        root2 = TreeNode(3,
                         TreeNode(5, TreeNode(6), TreeNode(7)),
                         TreeNode(1,
                                  TreeNode(4),
                                  TreeNode(2, TreeNode(9), TreeNode(8))))
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.leafSimilar(root1, root2), output)

    def test_example2(self):
        # Input
        root1 = TreeNode(1)
        root2 = TreeNode(1)
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.leafSimilar(root1, root2), output)

    def test_example3(self):
        # Input
        root1 = TreeNode(1)
        root2 = TreeNode(2)
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.leafSimilar(root1, root2), output)

    def test_example4(self):
        # Input
        root1 = TreeNode(1, TreeNode(2))
        root2 = TreeNode(2, TreeNode(2))
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.leafSimilar(root1, root2), output)

    def test_example5(self):
        # Input
        root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        root2 = TreeNode(1, TreeNode(3), TreeNode(2))
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.leafSimilar(root1, root2), output)


if __name__ == "__main__":
    unittest.main()

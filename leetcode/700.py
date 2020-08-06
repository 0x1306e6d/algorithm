"""
    File: 700.py
    Title: Search in a Binary Search Tree
    Difficulty: Easy
    URL: https://leetcode.com/problems/search-in-a-binary-search-tree/
"""

import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, value):
        return self.val == value.val


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root
        while current:
            if current.val == val:
                return current
            elif current.val > val:
                current = current.left
            else:
                current = current.right
        return None


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        val = 2
        # Output
        output = TreeNode(2, TreeNode(1), TreeNode(3))

        solution = Solution()
        self.assertEqual(solution.searchBST(root, val), output)


if __name__ == "__main__":
    unittest.main()

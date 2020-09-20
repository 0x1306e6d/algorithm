"""
    File: 106.py
    Title: Construct Binary Tree from Inorder and Postorder Traversal
    Difficulty: Medium
    URL: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root_value = postorder[-1]
        root_index_in_inorder = inorder.index(root_value)

        left_inorder = inorder[:root_index_in_inorder]
        left_postorder = postorder[:root_index_in_inorder]
        left = self.buildTree(left_inorder, left_postorder)

        right_inorder = inorder[root_index_in_inorder + 1:]
        right_postorder = postorder[root_index_in_inorder:-1]
        right = self.buildTree(right_inorder, right_postorder)

        return TreeNode(root_value, left, right)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        # Output
        output = TreeNode(3,
                          TreeNode(9),
                          TreeNode(20, TreeNode(15), TreeNode(7)))

        solution = Solution()
        self.assertEqual(solution.buildTree(inorder, postorder), output)


if __name__ == "__main__":
    unittest.main()

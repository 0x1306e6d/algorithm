"""
    File: 889.py
    Title: Construct Binary Tree from Preorder and Postorder Traversal
    Difficulty: Medium
    URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
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
    def constructFromPrePost(self,
                             preorder: List[int],
                             postorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_value = postorder[-1]

        right_root_value = postorder[-2]
        right_root_index_in_preorder = preorder.index(right_root_value)

        left_preorder = preorder[1:right_root_index_in_preorder]
        left_postorder = postorder[:(right_root_index_in_preorder - 1)]
        left = self.constructFromPrePost(left_preorder, left_postorder)

        right_preorder = preorder[right_root_index_in_preorder:]
        right_postorder = postorder[(right_root_index_in_preorder - 1):-1]
        right = self.constructFromPrePost(right_preorder, right_postorder)

        return TreeNode(root_value, left, right)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        pre = [1, 2, 4, 5, 3, 6, 7]
        post = [4, 5, 2, 6, 7, 3, 1]
        # Output
        output = TreeNode(1,
                          TreeNode(2, TreeNode(4), TreeNode(5)),
                          TreeNode(3, TreeNode(6), TreeNode(7)))

        solution = Solution()
        self.assertEqual(solution.constructFromPrePost(pre, post), output)


if __name__ == "__main__":
    unittest.main()

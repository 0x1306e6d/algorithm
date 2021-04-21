"""
    File: 1609.py
    Title: Even Odd Tree
    Difficulty: Medium
    URL: https://leetcode.com/problems/even-odd-tree/
"""

import unittest

from collections import deque
from typing import List


class TreeNode:
    def __init__(self,
                 val: int,
                 left: "TreeNode" = None,
                 right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        odd_q = deque()
        even_q = deque()

        odd_q.append(root)
        while True:
            odd_val = None
            while odd_q:
                current = odd_q.popleft()

                if (current.val % 2) == 0:
                    return False

                if odd_val is not None:
                    if odd_val >= current.val:
                        return False
                odd_val = current.val

                if current.left is not None:
                    even_q.append(current.left)
                if current.right is not None:
                    even_q.append(current.right)

            even_val = None
            while even_q:
                current = even_q.popleft()

                if (current.val % 2) == 1:
                    return False

                if even_val is not None:
                    if even_val <= current.val:
                        return False
                even_val = current.val

                if current.left is not None:
                    odd_q.append(current.left)
                if current.right is not None:
                    odd_q.append(current.right)

            if not odd_q:
                break

        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(1,
                        TreeNode(10,
                                 TreeNode(3,
                                          TreeNode(12),
                                          TreeNode(8))),
                        TreeNode(4,
                                 TreeNode(7, TreeNode(6)),
                                 TreeNode(9, None, TreeNode(2))))
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isEvenOddTree(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(5,
                        TreeNode(4, TreeNode(3), TreeNode(7)),
                        TreeNode(2, TreeNode(7)))
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isEvenOddTree(root), output)

    def test_example3(self):
        # Input
        root = TreeNode(5,
                        TreeNode(9, TreeNode(3), TreeNode(5)),
                        TreeNode(1, TreeNode(7)))
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isEvenOddTree(root), output)

    def test_example4(self):
        # Input
        root = TreeNode(1)
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isEvenOddTree(root), output)

    def test_example5(self):
        # Input
        root = TreeNode(11,
                        TreeNode(8,
                                 TreeNode(1,
                                          TreeNode(30, TreeNode(17)),
                                          TreeNode(20)),
                                 TreeNode(3,
                                          TreeNode(18),
                                          TreeNode(16))),
                        TreeNode(6,
                                 TreeNode(9,
                                          TreeNode(12),
                                          TreeNode(10)),
                                 TreeNode(11,
                                          TreeNode(4),
                                          TreeNode(2))))
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isEvenOddTree(root), output)


if __name__ == "__main__":
    unittest.main()

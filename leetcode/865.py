"""
    File: 865.py
    Title: Smallest Subtree with all the Deepest Nodes
    Difficulty: Medium
    URL: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
"""

import unittest

from typing import List


class TreeNode:
    def __init__(self,
                 val: int,
                 left: "TreeNode" = None,
                 right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, o) -> bool:
        if o is None:
            return False
        return self.val == o.val and \
            self.left == o.left and self.right == o.right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        nodes = {}
        parents = {}
        distances = {}

        def dfs(node: TreeNode, distance: int = 0) -> None:
            nodes[node.val] = node

            if distance not in distances:
                distances[distance] = []

            distances[distance].append(node.val)

            if node.left is not None:
                parents[node.left.val] = node.val
                dfs(node.left, distance + 1)
            if node.right is not None:
                parents[node.right.val] = node.val
                dfs(node.right, distance + 1)

        dfs(root)

        smallest_subtree = set(distances[max(distances.keys())])
        while len(smallest_subtree) > 1:
            next_smallest_subtree = set()
            for node in smallest_subtree:
                if node == root.val:
                    next_smallest_subtree.add(node)
                else:
                    next_smallest_subtree.add(parents[node])
                smallest_subtree = next_smallest_subtree
        return nodes[smallest_subtree.pop()]


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(3,
                        TreeNode(5,
                                 TreeNode(6),
                                 TreeNode(2, TreeNode(7), TreeNode(4))),
                        TreeNode(1, TreeNode(0), TreeNode(8)))
        # Output
        output = TreeNode(2, TreeNode(7), TreeNode(4))

        solution = Solution()
        self.assertEqual(solution.subtreeWithAllDeepest(root), output)

    def test_example2(self):
        # Input
        root = TreeNode(1)
        # Output
        output = TreeNode(1)

        solution = Solution()
        self.assertEqual(solution.subtreeWithAllDeepest(root), output)

    def test_example3(self):
        # Input
        root = TreeNode(0,
                        TreeNode(1,
                                 None,
                                 TreeNode(2)),
                        TreeNode(3))
        # Output
        output = TreeNode(2)

        solution = Solution()
        self.assertEqual(solution.subtreeWithAllDeepest(root), output)


if __name__ == "__main__":
    unittest.main()

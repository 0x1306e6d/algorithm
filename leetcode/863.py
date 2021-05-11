"""
    File: 863.py
    Title: All Nodes Distance K in Binary Tree
    Difficulty: Medium
    URL: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""

import unittest

from collections import defaultdict
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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        target_node = target.val

        graph = defaultdict(list)

        def graphfy(node: TreeNode):
            graph[node.val]
            if node.left is not None:
                graph[node.val].append(node.left.val)
                graphfy(node.left)
                graph[node.left.val].append(node.val)
            if node.right is not None:
                graph[node.val].append(node.right.val)
                graphfy(node.right)
                graph[node.right.val].append(node.val)

        graphfy(root)

        ans = [target_node]
        visited = [False] * (len(graph) + 1)
        visited[target_node] = True
        for i in range(k):
            next_ans = []
            for node in ans:
                for adjacent in graph[node]:
                    if not visited[adjacent]:
                        next_ans.append(adjacent)
                    visited[adjacent] = True
                visited[node] = True
            ans = next_ans
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        root = TreeNode(3,
                        TreeNode(5,
                                 TreeNode(6),
                                 TreeNode(2, TreeNode(7), TreeNode(4))),
                        TreeNode(1, TreeNode(0), TreeNode(8)))
        target = TreeNode(5)
        k = 2
        # Output
        output = [7, 4, 1]

        solution = Solution()
        self.assertEqual(solution.distanceK(root, target, k), output)


if __name__ == "__main__":
    unittest.main()

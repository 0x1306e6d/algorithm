"""
    File: 834.py
    Title: Sum of Distances in Tree
    Difficulty: Hard
    URL: https://leetcode.com/problems/sum-of-distances-in-tree/
"""

import unittest

from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(n)]
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)

        counts = [1] * n
        ans = [0] * n

        def post(root: int, previous: int):
            for i in tree[root]:
                if i != previous:
                    post(i, root)
                    counts[root] += counts[i]
                    ans[root] += (ans[i] + counts[i])
        post(0, -1)

        def pre(root: int, previous: int):
            for i in tree[root]:
                if i != previous:
                    ans[i] = ans[root] - counts[i] + (n - counts[i])
                    pre(i, root)
            pass
        pre(0, -1)

        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 6
        edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
        # Output
        output = [8, 12, 6, 10, 10, 10]

        solution = Solution()
        self.assertEqual(solution.sumOfDistancesInTree(n, edges), output)


if __name__ == "__main__":
    unittest.main()

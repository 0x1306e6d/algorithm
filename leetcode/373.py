"""
    File: 373.py
    Title: Find K Pairs with Smallest Sums
    Difficulty: Medium
    URL: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""

import unittest

from typing import List


class Solution:
    def kSmallestPairs(self,
                       nums1: List[int],
                       nums2: List[int],
                       k: int) -> List[List[int]]:
        memo = {}
        for u in nums1:
            for v in nums2:
                uv = u + v
                if uv not in memo:
                    memo[uv] = []
                memo[uv].append([u, v])

        pairs = []
        for key in sorted(memo):
            for pair in memo[key]:
                pairs.append(pair)
                if len(pairs) == k:
                    break
            if len(pairs) == k:
                break
        return pairs


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 3
        # Output
        output = [[1, 2], [1, 4], [1, 6]]

        solution = Solution()
        self.assertEqual(solution.kSmallestPairs(nums1, nums2, k), output)

    def test_example2(self):
        # Input
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 2
        # Output
        output = [[1, 1], [1, 1]]

        solution = Solution()
        self.assertEqual(solution.kSmallestPairs(nums1, nums2, k), output)

    def test_example3(self):
        # Input
        nums1 = [1, 2]
        nums2 = [3]
        k = 3
        # Output
        output = [[1, 3], [2, 3]]

        solution = Solution()
        self.assertEqual(solution.kSmallestPairs(nums1, nums2, k), output)


if __name__ == "__main__":
    unittest.main()

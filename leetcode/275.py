"""
    File: 275.py
    Title: H-Index II
    Difficulty: Medium
    URL: https://leetcode.com/problems/h-index-ii/
"""

import unittest

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        for i, citation in enumerate(citations):
            if citation >= length - i:
                return length - i
        return 0


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        citations = [0, 1, 3, 5, 6]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.hIndex(citations), output)


if __name__ == "__main__":
    unittest.main()

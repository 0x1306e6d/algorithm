"""
    File: 565.py
    Title: Array Nesting
    Difficulty: Medium
    URL: https://leetcode.com/problems/array-nesting/
"""

import unittest

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)

        maximum = 0
        for i in range(len(nums)):
            if visited[i]:
                continue

            s = set()
            j = i
            while j not in s:
                s.add(j)
                j = nums[j]
            for k in s:
                visited[k] = True
            maximum = max(maximum, len(s))

        return maximum


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [5, 4, 0, 3, 1, 6, 2]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.arrayNesting(nums), output)


if __name__ == "__main__":
    unittest.main()

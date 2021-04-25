"""
    File: 1748.py
    Title: Sum of Unique Elements
    Difficulty: Easy
    URL: https://leetcode.com/problems/sum-of-unique-elements/
"""

import unittest

from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0

        visited = [0] * 101
        for n in nums:
            if visited[n] == 0:
                ans += n
            elif visited[n] == 1:
                ans -= n
            visited[n] += 1

        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        nums = [1, 2, 3, 2]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.sumOfUnique(nums), output)

    def test_example2(self):
        # Input
        nums = [1, 1, 1, 1, 1]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.sumOfUnique(nums), output)

    def test_example3(self):
        # Input
        nums = [1, 2, 3, 4, 5]
        # Output
        output = 15

        solution = Solution()
        self.assertEqual(solution.sumOfUnique(nums), output)


if __name__ == "__main__":
    unittest.main()

"""
    File: 1200.py
    Title: Minimum Absolute Difference
    Difficulty: Easy
    URL: https://leetcode.com/problems/minimum-absolute-difference/
"""

import unittest

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = list(sorted(arr))

        minimum_diff = 987654321
        for i in range(1, len(arr)):
            minimum_diff = min(minimum_diff, arr[i] - arr[i - 1])
            if minimum_diff == 1:
                break

        ans = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == minimum_diff:
                ans.append([arr[i - 1], arr[i]])
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [4, 2, 1, 3]
        # Output
        output = [[1, 2], [2, 3], [3, 4]]

        solution = Solution()
        self.assertEqual(solution.minimumAbsDifference(arr), output)

    def test_example2(self):
        # Input
        arr = [1, 3, 6, 10, 15]
        # Output
        output = [[1, 3]]

        solution = Solution()
        self.assertEqual(solution.minimumAbsDifference(arr), output)

    def test_example3(self):
        # Input
        arr = [3, 8, -10, 23, 19, -4, -14, 27]
        # Output
        output = [[-14, -10], [19, 23], [23, 27]]

        solution = Solution()
        self.assertEqual(solution.minimumAbsDifference(arr), output)


if __name__ == "__main__":
    unittest.main()

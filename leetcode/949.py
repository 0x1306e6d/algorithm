"""
    File: 949.py
    Title: Largest Time for Given Digits
    Difficulty: Medium
    URL: https://leetcode.com/problems/largest-time-for-given-digits/
"""

import unittest

from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        largest = -1
        for (i, j, k, l) in permutations(range(4)):
            hour = (arr[i] * 10) + arr[j]
            if hour > 23:
                continue
            minute = (arr[k]*10) + arr[l]
            if minute > 59:
                continue
            time = (hour * 100) + minute
            largest = max(largest, time)

        if largest == -1:
            return ""

        hour = largest // 100
        if hour < 10:
            hour = "0" + str(hour)
        minute = largest % 100
        if minute < 10:
            minute = "0" + str(minute)
        return f"{hour}:{minute}"


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [1, 2, 3, 4]
        # Output
        output = "23:41"

        solution = Solution()
        self.assertEqual(solution.largestTimeFromDigits(arr), output)

    def test_example2(self):
        # Input
        arr = [5, 5, 5, 5]
        # Output
        output = ""

        solution = Solution()
        self.assertEqual(solution.largestTimeFromDigits(arr), output)


if __name__ == "__main__":
    unittest.main()

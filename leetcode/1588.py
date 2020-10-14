"""
    File: 1588.py
    Title: Sum of All Odd Length Subarrays
    Difficulty: Easy
    URL: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""

import unittest

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i) % 2 == 0:
                    answer += sum(arr[i:j + 1])
        return answer


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [1, 4, 2, 5, 3]
        # Output
        output = 58

        solution = Solution()
        self.assertEqual(solution.sumOddLengthSubarrays(arr), output)

    def test_example2(self):
        # Input
        arr = [1, 2]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.sumOddLengthSubarrays(arr), output)

    def test_example3(self):
        # Input
        arr = [10, 11, 12]
        # Output
        output = 66

        solution = Solution()
        self.assertEqual(solution.sumOddLengthSubarrays(arr), output)


if __name__ == "__main__":
    unittest.main()

"""
    File: 1346.py
    Title: Check If N and Its Double Exist
    Difficulty: Easy
    URL: https://leetcode.com/problems/check-if-n-and-its-double-exist/
"""

import unittest

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        for n in s:
            if n == 0:
                if arr.count(0) >= 2:
                    return True
                continue

            if (n * 2) in s:
                return True
            if (n % 2) == 0 and (n // 2) in s:
                return True
        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        arr = [10, 2, 5, 3]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.checkIfExist(arr), output)

    def test_example2(self):
        # Input
        arr = [7, 1, 14, 11]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.checkIfExist(arr), output)

    def test_example3(self):
        # Input
        arr = [3, 1, 7, 11]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.checkIfExist(arr), output)

    def test_example4(self):
        # Input
        arr = [-2, 0, 10, -19, 4, 6, -8]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.checkIfExist(arr), output)


if __name__ == "__main__":
    unittest.main()

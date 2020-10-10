"""
    File: 342.py
    Title: Power of Four
    Difficulty: Easy
    URL: https://leetcode.com/problems/power-of-four/
"""

import unittest


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            if (num % 4) != 0:
                return False
            num //= 4
        return num == 1


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num = 16
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isPowerOfFour(num), output)

    def test_example2(self):
        # Input
        num = 5
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isPowerOfFour(num), output)


if __name__ == "__main__":
    unittest.main()

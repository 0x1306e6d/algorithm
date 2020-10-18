"""
    File: 231.py
    Title: Power of Two
    Difficulty: Easy
    URL: https://leetcode.com/problems/two-sum/
"""

import unittest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if (n % 2) == 1:
            return False
        return self.isPowerOfTwo(n // 2)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 1
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isPowerOfTwo(n), output)

    def test_example2(self):
        # Input
        n = 16
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isPowerOfTwo(n), output)

    def test_example3(self):
        # Input
        n = 3
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isPowerOfTwo(n), output)

    def test_example4(self):
        # Input
        n = 4
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isPowerOfTwo(n), output)

    def test_example5(self):
        # Input
        n = 5
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isPowerOfTwo(n), output)


if __name__ == "__main__":
    unittest.main()

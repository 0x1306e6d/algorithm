"""
    File: 326.py
    Title: Power of Three
    Difficulty: Easy
    URL: https://leetcode.com/problems/power-of-three/
"""

import unittest


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 27
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isPowerOfThree(n), output)

    def test_example2(self):
        # Input
        n = 0
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isPowerOfThree(n), output)

    def test_example3(self):
        # Input
        n = 9
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isPowerOfThree(n), output)

    def test_example4(self):
        # Input
        n = 45
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isPowerOfThree(n), output)


if __name__ == "__main__":
    unittest.main()

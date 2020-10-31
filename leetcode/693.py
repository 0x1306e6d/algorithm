"""
    File: 693.py
    Title: Binary Number with Alternating Bits
    Difficulty: Easy
    URL: https://leetcode.com/problems/binary-number-with-alternating-bits/
"""

import unittest


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        m = None
        while n > 0:
            if m is None:
                m = n % 2
            else:
                next_m = n % 2
                if next_m == m:
                    return False
                m = next_m
            n //= 2
        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 5
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.hasAlternatingBits(n), output)

    def test_example2(self):
        # Input
        n = 7
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.hasAlternatingBits(n), output)

    def test_example3(self):
        # Input
        n = 11
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.hasAlternatingBits(n), output)

    def test_example4(self):
        # Input
        n = 10
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.hasAlternatingBits(n), output)

    def test_example5(self):
        # Input
        n = 3
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.hasAlternatingBits(n), output)


if __name__ == "__main__":
    unittest.main()

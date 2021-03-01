"""
    File: 476.py
    Title: Number Complement
    Difficulty: Easy
    URL: https://leetcode.com/problems/number-complement/
"""

import unittest


class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0

        upper_bound = 1
        while upper_bound < num:
            upper_bound *= 2

        if num == upper_bound:
            return num - 1
        return (upper_bound - 1) ^ num


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num = 5
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.findComplement(num), output)

    def test_example2(self):
        # Input
        num = 1
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.findComplement(num), output)


if __name__ == "__main__":
    unittest.main()

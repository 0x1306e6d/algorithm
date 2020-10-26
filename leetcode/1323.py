"""
    File: 1323.py
    Title: Maximum 69 Number
    Difficulty: Easy
    URL: https://leetcode.com/problems/maximum-69-number/
"""

import unittest


class Solution:
    def maximum69Number(self, num: int) -> int:
        maximum = ""
        changed = False
        for c in str(num):
            if c == '9':
                maximum += c
            else:
                if not changed:
                    maximum += '9'
                    changed = True
                else:
                    maximum += c
        return int(maximum)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num = 9669
        # Output
        output = 9969

        solution = Solution()
        self.assertEqual(solution.maximum69Number(num), output)

    def test_example2(self):
        # Input
        num = 9996
        # Output
        output = 9999

        solution = Solution()
        self.assertEqual(solution.maximum69Number(num), output)

    def test_example3(self):
        # Input
        num = 9999
        # Output
        output = 9999

        solution = Solution()
        self.assertEqual(solution.maximum69Number(num), output)


if __name__ == "__main__":
    unittest.main()

"""
    File: 415.py
    Title: Add Strings
    Difficulty: Easy
    URL: https://leetcode.com/problems/add-strings/
"""

import unittest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        zero = ord('0')

        def atoi(s: str) -> int:
            i = 0
            for c in s:
                i += (ord(c) - zero)
                i *= 10
            return i // 10

        def itoa(i: int) -> str:
            if i == 0:
                return "0"

            s = ""
            while i > 0:
                s = chr(zero + (i % 10)) + s
                i //= 10
            return s

        return itoa(atoi(num1) + atoi(num2))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num1 = "11"
        num2 = "123"
        # Output
        output = "134"

        solution = Solution()
        self.assertEqual(solution.addStrings(num1, num2), output)

    def test_example2(self):
        # Input
        num1 = "456"
        num2 = "77"
        # Output
        output = "533"

        solution = Solution()
        self.assertEqual(solution.addStrings(num1, num2), output)

    def test_example3(self):
        # Input
        num1 = "0"
        num2 = "0"
        # Output
        output = "0"

        solution = Solution()
        self.assertEqual(solution.addStrings(num1, num2), output)


if __name__ == "__main__":
    unittest.main()

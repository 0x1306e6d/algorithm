"""
    File: 405.py
    Title: Convert a Number to Hexadecimal
    Difficulty: Easy
    URL: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
"""

import unittest


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num = 0xffffffff + num + 1

        hex_str = ""
        while True:
            d = num % 16
            if d >= 10:
                hex_str = chr(ord('a') + (d - 10)) + hex_str
            else:
                hex_str = chr(ord('0') + d) + hex_str

            num //= 16
            if num == 0:
                break

        return hex_str


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num = 26
        # Output
        output = "1a"

        solution = Solution()
        self.assertEqual(solution.toHex(num), output)

    def test_example2(self):
        # Input
        num = -1
        # Output
        output = "ffffffff"

        solution = Solution()
        self.assertEqual(solution.toHex(num), output)


if __name__ == "__main__":
    unittest.main()

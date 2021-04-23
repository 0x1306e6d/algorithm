"""
    File: 13.py
    Title: Roman to Integer
    Difficulty: Easy
    URL: https://leetcode.com/problems/roman-to-integer/
"""

import unittest


class Solution:
    def romanToInt(self, roman: str) -> int:
        symbols = {
            'I': {
                '': 1,
                'V': 4,
                'X': 9,
            },
            'V': {
                '': 5
            },
            'X': {
                '': 10,
                'L': 40,
                'C': 90,
            },
            'L': {
                '': 50
            },
            'C': {
                '': 100,
                'D': 400,
                'M': 900,
            },
            'D': {
                '': 500
            },
            'M': {
                '': 1000
            }
        }

        ans = 0
        i = 0
        while i < len(roman):
            symbol = roman[i]

            if (i + 1) < len(roman):
                next_symbol = roman[i + 1]
                if next_symbol in symbols[symbol]:
                    ans += symbols[symbol][next_symbol]
                    i += 1
                else:
                    ans += symbols[symbol]['']
            else:
                ans += symbols[symbol]['']

            i += 1

        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        roman = "III"
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.romanToInt(roman), output)

    def test_example2(self):
        # Input
        roman = "IV"
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.romanToInt(roman), output)

    def test_example3(self):
        # Input
        roman = "IX"
        # Output
        output = 9

        solution = Solution()
        self.assertEqual(solution.romanToInt(roman), output)

    def test_example4(self):
        # Input
        roman = "MCMXCIV"
        # Output
        output = 1994

        solution = Solution()
        self.assertEqual(solution.romanToInt(roman), output)


if __name__ == "__main__":
    unittest.main()

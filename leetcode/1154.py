"""
    File: 1154.py
    Title: Day of the Year
    Difficulty: Easy
    URL: https://leetcode.com/problems/day-of-the-year/
"""

import unittest


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = list(map(int, date.split('-')))
        is_leap = False
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    is_leap = True
            else:
                is_leap = True

        day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap:
            day_of_month[1] = 29

        day_of_year = 0
        for i in range(month - 1):
            day_of_year += day_of_month[i]
        day_of_year += day
        return day_of_year


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        date = "2019-01-09"
        # Output
        output = 9

        solution = Solution()
        self.assertEqual(solution.dayOfYear(date), output)

    def test_example2(self):
        # Input
        date = "2019-02-10"
        # Output
        output = 41

        solution = Solution()
        self.assertEqual(solution.dayOfYear(date), output)

    def test_example3(self):
        # Input
        date = "2003-03-01"
        # Output
        output = 60

        solution = Solution()
        self.assertEqual(solution.dayOfYear(date), output)

    def test_example4(self):
        # Input
        date = "2004-03-01"
        # Output
        output = 61

        solution = Solution()
        self.assertEqual(solution.dayOfYear(date), output)


if __name__ == "__main__":
    unittest.main()

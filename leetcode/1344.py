"""
    File: 1344.py
    Title: Angle Between Hands of a Clock
    Difficulty: Medium
    URL: https://leetcode.com/problems/angle-between-hands-of-a-clock/
"""

import unittest


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (360 / 12) * hour if hour != 12 else 0
        hour_angle += (30 / 60) * minutes
        minute_angle = (360 / 60) * minutes
        if hour_angle > minute_angle:
            return min(hour_angle - minute_angle,
                       360 - hour_angle + minute_angle)
        else:
            return min(minute_angle - hour_angle,
                       360 - minute_angle + hour_angle)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        hour = 12
        minutes = 30
        # Output
        output = 165

        solution = Solution()
        self.assertEqual(solution.angleClock(hour, minutes), output)

    def test_example2(self):
        # Input
        hour = 3
        minutes = 30
        # Output
        output = 75

        solution = Solution()
        self.assertEqual(solution.angleClock(hour, minutes), output)

    def test_example3(self):
        # Input
        hour = 3
        minutes = 15
        # Output
        output = 7.5

        solution = Solution()
        self.assertEqual(solution.angleClock(hour, minutes), output)

    def test_example4(self):
        # Input
        hour = 4
        minutes = 50
        # Output
        output = 155

        solution = Solution()
        self.assertEqual(solution.angleClock(hour, minutes), output)

    def test_example5(self):
        # Input
        hour = 12
        minutes = 0
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.angleClock(hour, minutes), output)


if __name__ == "__main__":
    unittest.main()

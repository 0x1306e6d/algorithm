"""
    File: 1529.py
    Title: Bulb Switcher IV
    Difficulty: Medium
    URL: https://leetcode.com/problems/bulb-switcher-iv/
"""

import unittest


class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        last = "0"
        for bulb in target:
            if bulb == last:
                continue
            else:
                last = bulb
                flips += 1
        return flips


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        target = "10111"
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.minFlips(target), output)

    def test_example2(self):
        # Input
        target = "101"
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.minFlips(target), output)

    def test_example3(self):
        # Input
        target = "00000"
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.minFlips(target), output)

    def test_example4(self):
        # Input
        target = "001011101"
        # Output
        output = 5

        solution = Solution()
        self.assertEqual(solution.minFlips(target), output)


if __name__ == "__main__":
    unittest.main()

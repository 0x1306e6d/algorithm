"""
    File: 1663.py
    Title: Smallest String With A Given Numeric Value
    Difficulty: Medium
    URL: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
"""

import unittest


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        smallest = ["a"] * n

        a = ord('a')

        i = n - 1
        remaining = k - n
        while remaining:
            biggest = min(remaining, 25)
            smallest[i] = chr(a + biggest)

            remaining -= biggest
            i -= 1

        return "".join(smallest)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        n = 3
        k = 27
        # Output
        output = "aay"

        solution = Solution()
        self.assertEqual(solution.getSmallestString(n, k), output)

    def test_example2(self):
        # Input
        n = 5
        k = 73
        # Output
        output = "aaszz"

        solution = Solution()
        self.assertEqual(solution.getSmallestString(n, k), output)


if __name__ == "__main__":
    unittest.main()

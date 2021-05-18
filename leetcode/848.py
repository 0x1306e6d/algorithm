"""
    File: 848.py
    Title: Shifting Letters
    Difficulty: Medium
    URL: https://leetcode.com/problems/shifting-letters/
"""

import unittest

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i + 1]) % 26

        a = ord('a')
        ans = []
        for i, shift in enumerate(shifts):
            ans.append(chr(((ord(s[i]) - a + shift) % 26) + a))
        return "".join(ans)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        s = "abc"
        shifts = [3, 5, 9]
        # Output
        output = "rpl"

        solution = Solution()
        self.assertEqual(solution.shiftingLetters(s, shifts), output)


if __name__ == "__main__":
    unittest.main()

"""
    File: 717.py
    Title: 1-bit and 2-bit Characters
    Difficulty: Easy
    URL: https://leetcode.com/problems/1-bit-and-2-bit-characters/
"""

import unittest

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        binary = ''.join([str(bit) for bit in bits])

        i = 0
        while i < (n - 1):
            if binary[i] == '0':
                i += 1
            else:
                i += 2

        if i == (n - 1):
            return True
        else:
            return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        bits = [1, 0, 0]
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.isOneBitCharacter(bits), output)

    def test_example2(self):
        # Input
        bits = [1, 1, 1, 0]
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.isOneBitCharacter(bits), output)


if __name__ == "__main__":
    unittest.main()

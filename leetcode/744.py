"""
    File: 744.py
    Title: Find Smallest Letter Greater Than Target
    Difficulty: Easy
    URL: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""

import unittest

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        next_letter = letters[0]
        for letter in letters:
            if letter > target:
                next_letter = letter
                break
        return next_letter


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        letters = ["c", "f", "j"]
        target = "a"
        # Output
        output = "c"

        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(letters, target), output)

    def test_example2(self):
        # Input
        letters = ["c", "f", "j"]
        target = "c"
        # Output
        output = "f"

        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(letters, target), output)

    def test_example3(self):
        # Input
        letters = ["c", "f", "j"]
        target = "d"
        # Output
        output = "f"

        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(letters, target), output)

    def test_example4(self):
        # Input
        letters = ["c", "f", "j"]
        target = "g"
        # Output
        output = "j"

        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(letters, target), output)

    def test_example5(self):
        # Input
        letters = ["c", "f", "j"]
        target = "j"
        # Output
        output = "c"

        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(letters, target), output)

    def test_example6(self):
        # Input
        letters = ["c", "f", "j"]
        target = "k"
        # Output
        output = "c"

        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(letters, target), output)


if __name__ == "__main__":
    unittest.main()

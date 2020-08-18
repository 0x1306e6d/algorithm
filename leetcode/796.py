"""
    File: 796.py
    Title: Rotate String
    Difficulty: Easy
    URL: https://leetcode.com/problems/rotate-string/
"""

import unittest


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        len_b = len(B)
        for i in range(len(A)):
            if A[:i] == B[(len_b - i):] and A[i:] == B[:(len_b - i)]:
                return True

        return False


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        A = "abcde"
        B = "cdeab"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.rotateString(A, B), output)

    def test_example2(self):
        # Input
        A = "abcde"
        B = "abced"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.rotateString(A, B), output)


if __name__ == "__main__":
    unittest.main()

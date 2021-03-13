"""
    File: 223.py
    Title: Rectangle Area
    Difficulty: Medium
    URL: https://leetcode.com/problems/rectangle-area/
"""

import unittest


class Solution:
    def computeArea(self,
                    A: int,
                    B: int,
                    C: int,
                    D: int,
                    E: int,
                    F: int,
                    G: int,
                    H: int) -> int:
        if E < A:
            return self.computeArea(E, F, G, H, A, B, C, D)

        I, J = max(A, E), max(B, F)
        K, L = min(C, G), min(D, H)

        area = ((C - A) * (D - B)) + ((G - E) * (H - F))
        if (E > C) or (F > D) or (B > H):
            return area
        return area - ((K - I) * (L - J))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        A = -3
        B = 0
        C = 3
        D = 4
        E = 0
        F = -1
        G = 9
        H = 2
        # Output
        output = 45

        solution = Solution()
        self.assertEqual(solution.computeArea(A, B, C, D, E, F, G, H), output)


if __name__ == "__main__":
    unittest.main()

"""
    File: 838.py
    Title: Push Dominoes
    Difficulty: Medium
    URL: https://leetcode.com/problems/push-dominoes/
"""

import unittest


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pushed = list(dominoes)

        previous = '.'
        right_p = -1
        left_p = -1
        for p, domino in enumerate(dominoes):
            if domino == 'R':
                if previous == 'R':
                    for i in range(right_p, p):
                        pushed[i] = 'R'
                right_p = p
                previous = 'R'
            if domino == 'L':
                if right_p == -1:
                    for i in range(p):
                        pushed[i] = 'L'
                elif previous == 'R':
                    start = right_p
                    end = p
                    while end > start:
                        pushed[start] = 'R'
                        start += 1

                        pushed[end] = 'L'
                        end -= 1
                else:
                    for i in range(left_p, p):
                        pushed[i] = 'L'

                left_p = p
                previous = 'L'

        if right_p > left_p:
            for i in range(right_p, len(dominoes)):
                pushed[i] = 'R'

        return ''.join(pushed)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        dominoes = ".L.R...LR..L.."
        # Output
        output = "LL.RR.LLRRLL.."

        solution = Solution()
        self.assertEqual(solution.pushDominoes(dominoes), output)

    def test_example2(self):
        # Input
        dominoes = "RR.L"
        # Output
        output = "RR.L"

        solution = Solution()
        self.assertEqual(solution.pushDominoes(dominoes), output)


if __name__ == "__main__":
    unittest.main()

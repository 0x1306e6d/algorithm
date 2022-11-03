"""
    File: 1927.py
    Title: Sum Game
    Difficulty: Medium
    URL: https://leetcode.com/problems/sum-game/
"""

import unittest

from math import ceil

from math import ceil


class Solution:
    def sumGame(self, num: str) -> bool:
        first_half = num[:len(num) // 2]
        second_half = num[(len(num) // 2):]

        first_sum = 0
        first_question = 0
        for c in first_half:
            if c == '?':
                first_question += 1
            else:
                first_sum += int(c)

        second_sum = 0
        second_question = 0
        for c in second_half:
            if c == '?':
                second_question += 1
            else:
                second_sum += int(c)

        diff_sum = first_sum - second_sum
        diff_question = first_question - second_question
        if diff_question == 0:
            return diff_sum != 0
        if diff_sum > 0 and diff_question > 0:
            return True
        if diff_sum < 0 and diff_question < 0:
            return True

        diff_sum = abs(diff_sum)
        diff_question = abs(diff_question)
        if diff_question == 1:
            return True
        alice = ceil(diff_question / 2)
        bob = diff_question - alice
        if alice * 9 > diff_sum:
            return True
        if bob * 9 >= diff_sum:
            return False
        return True


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        num = "5023"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.sumGame(num), output)

    def test_example2(self):
        # Input
        num = "25??"
        # Output
        output = True

        solution = Solution()
        self.assertEqual(solution.sumGame(num), output)

    def test_example3(self):
        # Input
        num = "?3295???"
        # Output
        output = False

        solution = Solution()
        self.assertEqual(solution.sumGame(num), output)


if __name__ == "__main__":
    unittest.main()

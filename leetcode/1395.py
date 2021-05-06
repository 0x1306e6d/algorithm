"""
    File: 1395.py
    Title: Count Number of Teams
    Difficulty: Medium
    URL: https://leetcode.com/problems/count-number-of-teams/
"""

import unittest

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        memo = [{'up': None, 'down': None} for _ in range(len(rating))]

        ans = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    if memo[j]['up'] is not None:
                        ans += memo[j]['up']
                    else:
                        up = 0
                        for k in range(j + 1, len(rating)):
                            if rating[k] > rating[j]:
                                up += 1
                        memo[j]['up'] = up
                        ans += up
                else:
                    if memo[j]['down'] is not None:
                        ans += memo[j]['down']
                    else:
                        down = 0
                        for k in range(j + 1, len(rating)):
                            if rating[j] > rating[k]:
                                down += 1
                        memo[j]['down'] = down
                        ans += down
        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        rating = [2, 5, 3, 4, 1]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numTeams(rating), output)

    def test_example2(self):
        # Input
        rating = [2, 1, 3]
        # Output
        output = 0

        solution = Solution()
        self.assertEqual(solution.numTeams(rating), output)

    def test_example3(self):
        # Input
        rating = [1, 2, 3, 4]
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.numTeams(rating), output)


if __name__ == "__main__":
    unittest.main()

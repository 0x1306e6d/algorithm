"""
    File: 1103.py
    Title:  Distribute Candies to People
    Difficulty: Easy
    URL: https://leetcode.com/problems/distribute-candies-to-people/
"""

import unittest

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        distributed = [0] * num_people

        i = 0
        n = 1
        while candies > 0:
            distributed[i] += min(n, candies)
            candies -= n
            n += 1
            i = (i + 1) % num_people
        return distributed


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        candies = 7
        num_people = 4
        # Output
        output = [1, 2, 3, 1]

        solution = Solution()
        self.assertEqual(solution.distributeCandies(candies, num_people),
                         output)

    def test_example2(self):
        # Input
        candies = 10
        num_people = 3
        # Output
        output = [5, 2, 3]

        solution = Solution()
        self.assertEqual(solution.distributeCandies(candies, num_people),
                         output)


if __name__ == "__main__":
    unittest.main()

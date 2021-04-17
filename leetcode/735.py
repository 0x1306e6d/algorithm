"""
    File: 735.py
    Title: Asteroid Collision
    Difficulty: Medium
    URL: https://leetcode.com/problems/asteroid-collision/
"""

import unittest

from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for asteroid in asteroids:
            if len(ans) == 0:
                ans.append(asteroid)
            elif asteroid > 0:
                ans.append(asteroid)
            elif ans[-1] < 0:
                ans.append(asteroid)
            else:
                broken = False

                i = len(ans) - 1
                while i >= 0:
                    current = ans[i]
                    if current < 0:
                        break
                    if abs(current) > abs(asteroid):
                        broken = True
                        break
                    ans.pop(-1)
                    if abs(current) == abs(asteroid):
                        broken = True
                        break
                    i -= 1

                if not broken:
                    ans.append(asteroid)

        return ans


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        asteroids = [5, 10, -5]
        # Output
        output = [5, 10]

        solution = Solution()
        self.assertEqual(solution.asteroidCollision(asteroids), output)

    def test_example2(self):
        # Input
        asteroids = [8, -8]
        # Output
        output = []

        solution = Solution()
        self.assertEqual(solution.asteroidCollision(asteroids), output)

    def test_example3(self):
        # Input
        asteroids = [10, 2, -5]
        # Output
        output = [10]

        solution = Solution()
        self.assertEqual(solution.asteroidCollision(asteroids), output)

    def test_example4(self):
        # Input
        asteroids = [-2, -1, 1, 2]
        # Output
        output = [-2, -1, 1, 2]

        solution = Solution()
        self.assertEqual(solution.asteroidCollision(asteroids), output)


if __name__ == "__main__":
    unittest.main()

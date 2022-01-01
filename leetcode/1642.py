"""
    File: 1642.py
    Title: Furthest Building You Can Reach
    Difficulty: Medium
    URL: https://leetcode.com/problems/furthest-building-you-can-reach/
"""

import unittest

import heapq
from typing import List, Tuple


class Solution:
    def furthestBuilding(self,
                         heights: List[int],
                         bricks: int,
                         ladders: int) -> int:
        jumps = []
        current = 0
        for i, height in enumerate(heights):
            if current > 0 and height > current:
                jumps.append((height - current, i))
            current = height

        if ladders == 0:
            if bricks == 0:
                if len(jumps) == 0:
                    return len(heights) - 1
                else:
                    return jumps[0][1] - 1
            return self.furtest_building(heights, jumps, bricks)

        latest_jump_index = 0
        ladder_used = []
        remaining_bricks = bricks
        remaining_ladders = ladders
        for i, (jump, _) in enumerate(jumps):
            if remaining_ladders > 0:
                heapq.heappush(ladder_used, jump)
                remaining_ladders -= 1
                latest_jump_index = i
                continue

            smaller = min(jump, ladder_used[0])
            if remaining_bricks < smaller:
                break
            remaining_bricks -= smaller

            if jump > ladder_used[0]:
                heapq.heappop(ladder_used)
                heapq.heappush(ladder_used, jump)

            latest_jump_index = i

        if latest_jump_index == (len(jumps) - 1):
            return len(heights) - 1
        else:
            return jumps[latest_jump_index + 1][1] - 1

    def furtest_building(self,
                         heights: List[int],
                         jumps: List[Tuple[int, int]],
                         bricks: int) -> int:
        latest_jump_index = 0
        remaining_bricks = bricks
        for i, (jump, _) in enumerate(jumps):
            if remaining_bricks >= jump:
                remaining_bricks -= jump
                latest_jump_index = i
            else:
                break
        if latest_jump_index == (len(jumps) - 1):
            return len(heights) - 1
        else:
            return jumps[latest_jump_index + 1][1] - 1


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        heights = [4, 2, 7, 6, 9, 14, 12]
        bricks = 5
        ladders = 1
        # Output
        output = 4

        solution = Solution()
        self.assertEqual(solution.furthestBuilding(heights, bricks, ladders),
                         output)

    def test_example2(self):
        # Input
        heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
        bricks = 10
        ladders = 2
        # Output
        output = 7

        solution = Solution()
        self.assertEqual(solution.furthestBuilding(heights, bricks, ladders),
                         output)

    def test_example3(self):
        # Input
        heights = [14, 3, 19, 3]
        bricks = 17
        ladders = 0
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.furthestBuilding(heights, bricks, ladders),
                         output)


if __name__ == "__main__":
    unittest.main()

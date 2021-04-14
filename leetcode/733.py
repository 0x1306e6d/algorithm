"""
    File: 733.py
    Title: Flood Fill
    Difficulty: Easy
    URL: https://leetcode.com/problems/flood-fill/
"""

import unittest

from collections import deque
from typing import List


class Solution:
    def floodFill(self,
                  image: List[List[int]],
                  sr: int,
                  sc: int,
                  new_color: int) -> List[List[int]]:
        __dx__ = [0, 0, -1, 1]
        __dy__ = [-1, 1, 0, 0]

        height = len(image)
        width = len(image[0])
        origin_color = image[sr][sc]
        visited = [[False] * width for _ in range(height)]

        q = deque()
        q.append((sr, sc))
        visited[sr][sc] = True
        while q:
            r, c = q.popleft()

            image[r][c] = new_color

            for dx, dy in zip(__dx__, __dy__):
                nr = r + dx
                nc = c + dy
                if (0 <= nr < height) and (0 <= nc < width):
                    if not visited[nr][nc] and (image[nr][nc] == origin_color):
                        q.append((nr, nc))
                        visited[nr][nc] = True

        return image


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        new_color = 2
        # Output
        output = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

        solution = Solution()
        self.assertEqual(solution.floodFill(image, sr, sc, new_color), output)


if __name__ == "__main__":
    unittest.main()

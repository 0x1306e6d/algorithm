"""
    File: 661.py
    Title: Image Smoother
    Difficulty: Easy
"""

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        directions = [-1, 0, 1]

        ans = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                cell_sum = 0
                cell_count = 0
                for dy in directions:
                    for dx in directions:
                        x2, y2 = x + dx, y + dy
                        if 0 <= x2 < n and 0 <= y2 < m:
                            cell_sum += img[y2][x2]
                            cell_count += 1
                ans[y][x] = cell_sum // cell_count
        return ans

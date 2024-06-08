"""
    File: 531.py
    Title: Lonely Pixel I
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        rows = [0] * m
        cols = [0] * n
        for y in range(m):
            for x in range(n):
                if picture[y][x] == "B":
                    rows[y] += 1
                    cols[x] += 1
        ans = 0
        for y in range(m):
            for x in range(n):
                if picture[y][x] == "B":
                    if rows[y] == 1 and cols[x] == 1:
                        ans += 1
        return ans

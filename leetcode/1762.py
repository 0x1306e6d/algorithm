"""
    File: 1762.py
    Title: Buildings With an Ocean View
    Difficulty: Medium
"""

from collections import deque
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = deque()
        right = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > right:
                ans.appendleft(i)
                right = heights[i]
        return list(ans)

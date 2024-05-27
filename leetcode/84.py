"""
    File: 84.py
    Title: Largest Rectangle in Histogram
    Difficulty: Hard
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(heights)):
            h1 = heights[i]
            while stack and heights[stack[-1]] > h1:
                j = stack.pop()
                h2 = heights[j]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                ans = max(ans, h2 * width)
            stack.append(i)
        while stack:
            j = stack.pop()
            h2 = heights[j]
            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)
            ans = max(ans, h2 * width)
        return ans

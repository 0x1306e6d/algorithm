"""
    File: 135.py
    Title: Candy
    Difficulty: Hard
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        left = [0] * n
        left[0] = 1
        prev = ratings[0]
        for i in range(1, n):
            current = ratings[i]
            if current > prev:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
            prev = current

        right = [0] * n
        right[n - 1] = 1
        prev = ratings[n - 1]
        for i in range(n - 2, -1, -1):
            current = ratings[i]
            if current > prev:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
            prev = current

        ans = 0
        for i in range(n):
            ans += max(left[i], right[i])
        return ans

"""
    File: 77.py
    Title: Combinations
    Difficulty: Medium
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []

        def do_combine(arr):
            if len(arr) == k:
                self.ans.append(arr.copy())
            else:
                if arr:
                    minimum = arr[-1] + 1
                else:
                    minimum = 1
                for i in range(minimum, n + 1):
                    arr.append(i)
                    do_combine(arr)
                    arr.pop()

        do_combine([])
        return self.ans

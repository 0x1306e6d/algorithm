"""
    File: 39.py
    Title: Combination Sum
    Difficulty: Medium
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def backtrace(i, s, p):
            if s == target:
                self.ans.append(p.copy())
            elif s > target or i >= len(candidates):
                return
            else:
                backtrace(i + 1, s, p)

                n = candidates[i]
                p.append(n)
                backtrace(i, s + n, p)
                p.pop()

        backtrace(0, 0, [])

        return self.ans

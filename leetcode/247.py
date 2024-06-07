"""
    File: 247.py
    Title: Strobogrammatic Number II
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        ans = []

        def backtrace(i, j, arr):
            if i > j:
                ans.append("".join(arr))
            elif i == j:
                for c in ["0", "1", "8"]:
                    arr[i] = c
                    ans.append("".join(arr))
            else:
                for s, e in [
                    ["0", "0"],
                    ["1", "1"],
                    ["6", "9"],
                    ["8", "8"],
                    ["9", "6"],
                ]:
                    if i == 0 and s == "0":
                        continue
                    arr[i] = s
                    arr[j] = e
                    backtrace(i + 1, j - 1, arr)

        backtrace(0, n - 1, ["0"] * n)

        return ans

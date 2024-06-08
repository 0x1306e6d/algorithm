"""
    File: 484.py
    Title: Find Permutation
    Difficulty: Medium
"""

from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        ans = []
        stack = []
        for i in range(1, n + 1):
            c = s[i - 1] if i < n else "I"
            if c == "I":
                stack.append(i)
                while stack:
                    j = stack.pop()
                    ans.append(j)
            else:
                stack.append(i)
        return ans

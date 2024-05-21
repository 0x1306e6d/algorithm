"""
    File: 1347.py
    Title: Minimum Number of Steps to Make Two Strings Anagram
    Difficulty: Medium
"""

from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = defaultdict(int)
        for c in s:
            s_count[c] += 1
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1

        diff = 0
        for i in range(ord("a"), ord("z") + 1):
            c = chr(i)
            diff += abs(s_count[c] - t_count[c])
        if diff % 2 == 0:
            return diff // 2
        return diff // 2 + 1
